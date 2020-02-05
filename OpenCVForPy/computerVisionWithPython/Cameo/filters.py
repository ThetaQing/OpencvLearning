# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:48:28 2020
滤波器文件
@author: Administrator
"""
import cv2
import numpy
import utils

def strokeEdges(src, dst, blurKsize = 7, edgeKsize = 5):
    if blurKsize >= 3:
        blurredSrc = cv2.medianBlur(src, blurKsize)  # 模糊处理，缓解滤波函数将噪声错误地识别为边缘
        graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)  # 使用Laplacian函数之前，需要将图像从BGR色彩空间转为灰度空间
    else:
        graySrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize = edgeKsize)  # 边缘检测滤波函数，将边缘区域转为白色或者其他饱和的颜色
    # 在得到Laplacian()函数的结果之后，需要将其转换为黑色边缘和白色背景的图像，然后将其归一化，并乘以源图像以便能将边缘变黑
    normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel * normalizedInverseAlpha
    cv2.merge(channels, dst)
    
class VConvolutionFilter(object):
    # 表示一般的卷积滤波器
    def __init__(self, kernel):
        self._kernel = kernel
    def apply(self, src, dst):
        # 将这个滤波器应用在一个BGR/gray源/目标上
        cv2.filter2D(src, -1, self._kernel, dst)
        
class SharpenFilter(VConvolutionFilter):
    # 表示特定的锐化滤波器
    """
    A sharpen filter with a 1-pixel radius.
    注意权重加起来为1，如果不想改变图像的亮度修改锐化核使它的权重加起来为0，就会得到一个边缘检测核
    
    
    """
    def __init__(self):
        kernel = numpy.array([[-1, -1, -1],
                             [-1, 9, -1],
                             [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)
        
class FindEdgesFilter(VConvolutionFilter):
    """An edge-finding filter with a 1-pixel radius."""
    
    def __init__(self):
        kernel = numpy.array([[-1, -1, -1],
                              [-1, 8, -1],
                              [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)
        
class BlurFilter(VConvolutionFilter):
    """A blur filter with a 2-pixel radius."""
    
    def __init__(self):
        kernel = numpy.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04]])
        VConvolutionFilter.__init__(self, kernel)
        
class EmbossFilter(VConvolutionFilter):
    """An emboss filter with a 1-pixel radius."""
    
    def __init__(self):
        kernel = numpy.array([[-2, -1, 0],
                              [-1, 1, 1],
                              [0, 1, 2]])
        VConvolutionFilter.__init__(self, kernel)
        

class BGRFuncFilter(object):
    def __init__(self, vFunc = None, bFunc = None, gFunc = None, rFunc = None,dtype = numpy.uint8) :
        length = numpy.iinfo(dtype).max + 1
        self._bLookupArray = utils.createLookupArray(utils.createCompositeFunc(bFunc, vFunc), length)
        self._gLookupArray = utils.createLookupArray(utils.createCompositeFunc(gFunc, vFunc), length)
        self._rLookupArray = utils.createLookupArray(utils.createCompositeFunc(rFunc, vFunc), length)
    def apply(self, src, dst) :
        """Apply the filter with a BGR source/destination."""
        b, g, r = cv2.split(src)
        utils.applyLookupArray(self._bLookupArray, b, b)
        utils.applyLookupArray(self._gLookupArray, g, g)
        utils.applyLookupArray(self._rLookupArray, r, r)
        cv2.merge([ b, g, r ], dst)
class BGRCurveFilter(BGRFuncFilter):
    def __init__(self, vPoints = None, bPoints = None,gPoints = None, rPoints = None, dtype = numpy.uint8):
        BGRFuncFilter.__init__(self, utils.createCurveFunc(vPoints), utils.createCurveFunc(bPoints), utils.createCurveFunc(gPoints), utils.createCurveFunc(rPoints), dtype)
class BGRPortraCurveFilter(BGRCurveFilter):
    def __init__(self, dtype = numpy.uint8):
        BGRCurveFilter.__init__(
            self,
            vPoints = [ (0, 0), (23, 20), (157, 173), (255, 255) ],
            bPoints = [ (0, 0), (41, 46), (231, 228), (255, 255) ],
            gPoints = [ (0, 0), (52, 47), (189, 196), (255, 255) ],
            rPoints = [ (0, 0), (69, 69), (213, 218), (255, 255) ],
            dtype = dtype)

    
    