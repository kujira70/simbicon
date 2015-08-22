# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_MathLib', [dirname(__file__)])
        except ImportError:
            import _MathLib
            return _MathLib
        if fp is not None:
            try:
                _mod = imp.load_module('_MathLib', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _MathLib = swig_import_helper()
    del swig_import_helper
else:
    import _MathLib
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


import Utils
class Matrix(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Matrix, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Matrix, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _MathLib.new_Matrix(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _MathLib.delete_Matrix
    __del__ = lambda self: None

    def loadZero(self):
        return _MathLib.Matrix_loadZero(self)

    def loadIdentity(self):
        return _MathLib.Matrix_loadIdentity(self)

    def setToOuterproduct(self, a, b):
        return _MathLib.Matrix_setToOuterproduct(self, a, b)

    def resizeTo(self, m, n):
        return _MathLib.Matrix_resizeTo(self, m, n)

    def shallowCopy(self, other, startRow=0, startCol=0, endRow=-1, endCol=-1):
        return _MathLib.Matrix_shallowCopy(self, other, startRow, startCol, endRow, endCol)

    def deepCopy(self, other):
        return _MathLib.Matrix_deepCopy(self, other)

    def getColumnCount(self):
        return _MathLib.Matrix_getColumnCount(self)

    def getRowCount(self):
        return _MathLib.Matrix_getRowCount(self)

    def multiplyBy(self, val):
        return _MathLib.Matrix_multiplyBy(self, val)

    def setToProductOf(self, a, b, transA=False, transB=False):
        return _MathLib.Matrix_setToProductOf(self, a, b, transA, transB)

    def setToInverseOf(self, a, t=0):
        return _MathLib.Matrix_setToInverseOf(self, a, t)

    def printMatrix(self):
        return _MathLib.Matrix_printMatrix(self)

    def setToSubmatrix(self, a, i, j, rows, cols):
        return _MathLib.Matrix_setToSubmatrix(self, a, i, j, rows, cols)

    def get(self, i, j):
        return _MathLib.Matrix_get(self, i, j)

    def set(self, i, j, newVal):
        return _MathLib.Matrix_set(self, i, j, newVal)

    def setValues(self, vals):
        return _MathLib.Matrix_setValues(self, vals)

    def getMatrixPointer(self):
        return _MathLib.Matrix_getMatrixPointer(self)

    def __mul__(self, other):
        return _MathLib.Matrix___mul__(self, other)

    def postMultiplyVector(self, v, result):
        return _MathLib.Matrix_postMultiplyVector(self, v, result)

    def add(self, other, scaleA=1.0, scaleB=1.0):
        return _MathLib.Matrix_add(self, other, scaleA, scaleB)

    def sub(self, other, scaleA=1.0, scaleB=1.0):
        return _MathLib.Matrix_sub(self, other, scaleA, scaleB)
Matrix_swigregister = _MathLib.Matrix_swigregister
Matrix_swigregister(Matrix)


def testMatrixClass():
    return _MathLib.testMatrixClass()
testMatrixClass = _MathLib.testMatrixClass
class TransformationMatrix(Matrix):
    __swig_setmethods__ = {}
    for _s in [Matrix]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TransformationMatrix, name, value)
    __swig_getmethods__ = {}
    for _s in [Matrix]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, TransformationMatrix, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _MathLib.delete_TransformationMatrix
    __del__ = lambda self: None

    def __init__(self, *args):
        this = _MathLib.new_TransformationMatrix(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def setOGLValues(self, oglValues):
        return _MathLib.TransformationMatrix_setOGLValues(self, oglValues)

    def getValues(self, values):
        return _MathLib.TransformationMatrix_getValues(self, values)

    def getOGLValues(self, values):
        return _MathLib.TransformationMatrix_getOGLValues(self, values)

    def setToProductOf(self, *args):
        return _MathLib.TransformationMatrix_setToProductOf(self, *args)

    def setToTranslationMatrix(self, coords):
        return _MathLib.TransformationMatrix_setToTranslationMatrix(self, coords)

    def setToRotationMatrix(self, angle, axis):
        return _MathLib.TransformationMatrix_setToRotationMatrix(self, angle, axis)

    def __mul__(self, *args):
        return _MathLib.TransformationMatrix___mul__(self, *args)

    def getTranslation(self):
        return _MathLib.TransformationMatrix_getTranslation(self)

    def getLocalCoordTranslation(self):
        return _MathLib.TransformationMatrix_getLocalCoordTranslation(self)

    def setTranslation(self, *args):
        return _MathLib.TransformationMatrix_setTranslation(self, *args)

    def clearTranslation(self):
        return _MathLib.TransformationMatrix_clearTranslation(self)

    def setToTranspose(self):
        return _MathLib.TransformationMatrix_setToTranspose(self)

    def setToCoordFrameTransformation(self, x, y, z, origin):
        return _MathLib.TransformationMatrix_setToCoordFrameTransformation(self, x, y, z, origin)

    def setToInverseCoordFrameTransformation(self):
        return _MathLib.TransformationMatrix_setToInverseCoordFrameTransformation(self)

    def setToInverseCoordFrameTransformationOf(self, other):
        return _MathLib.TransformationMatrix_setToInverseCoordFrameTransformationOf(self, other)
TransformationMatrix_swigregister = _MathLib.TransformationMatrix_swigregister
TransformationMatrix_swigregister(TransformationMatrix)


def testTransformationMatrixClass():
    return _MathLib.testTransformationMatrixClass()
testTransformationMatrixClass = _MathLib.testTransformationMatrixClass
class Vector(Matrix):
    __swig_setmethods__ = {}
    for _s in [Matrix]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Vector, name, value)
    __swig_getmethods__ = {}
    for _s in [Matrix]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Vector, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _MathLib.new_Vector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _MathLib.delete_Vector
    __del__ = lambda self: None

    def shallowCopy(self, other):
        return _MathLib.Vector_shallowCopy(self, other)

    def deepCopy(self, other):
        return _MathLib.Vector_deepCopy(self, other)

    def setToProductOf(self, A, B, transA=False, transB=False):
        return _MathLib.Vector_setToProductOf(self, A, B, transA, transB)

    def setToRow(self, A, row, start=0, howMany=-1):
        return _MathLib.Vector_setToRow(self, A, row, start, howMany)

    def setToCol(self, A, col, start=0, howMany=-1):
        return _MathLib.Vector_setToCol(self, A, col, start, howMany)

    def printVector(self):
        return _MathLib.Vector_printVector(self)

    def get(self, i):
        return _MathLib.Vector_get(self, i)

    def set(self, i, newVal):
        return _MathLib.Vector_set(self, i, newVal)

    def normSquared(self):
        return _MathLib.Vector_normSquared(self)
Vector_swigregister = _MathLib.Vector_swigregister
Vector_swigregister(Vector)


def testVectorClass():
    return _MathLib.testVectorClass()
testVectorClass = _MathLib.testVectorClass
class ThreeTuple(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ThreeTuple, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ThreeTuple, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _MathLib.ThreeTuple_x_set
    __swig_getmethods__["x"] = _MathLib.ThreeTuple_x_get
    if _newclass:
        x = _swig_property(_MathLib.ThreeTuple_x_get, _MathLib.ThreeTuple_x_set)
    __swig_setmethods__["y"] = _MathLib.ThreeTuple_y_set
    __swig_getmethods__["y"] = _MathLib.ThreeTuple_y_get
    if _newclass:
        y = _swig_property(_MathLib.ThreeTuple_y_get, _MathLib.ThreeTuple_y_set)
    __swig_setmethods__["z"] = _MathLib.ThreeTuple_z_set
    __swig_getmethods__["z"] = _MathLib.ThreeTuple_z_get
    if _newclass:
        z = _swig_property(_MathLib.ThreeTuple_z_get, _MathLib.ThreeTuple_z_set)

    def __init__(self, *args):
        this = _MathLib.new_ThreeTuple(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _MathLib.delete_ThreeTuple
    __del__ = lambda self: None

    def getX(self):
        return _MathLib.ThreeTuple_getX(self)

    def getY(self):
        return _MathLib.ThreeTuple_getY(self)

    def getZ(self):
        return _MathLib.ThreeTuple_getZ(self)

    def setX(self, x):
        return _MathLib.ThreeTuple_setX(self, x)

    def setY(self, y):
        return _MathLib.ThreeTuple_setY(self, y)

    def setZ(self, z):
        return _MathLib.ThreeTuple_setZ(self, z)

    def setValues(self, *args):
        return _MathLib.ThreeTuple_setValues(self, *args)

    def __eq__(self, p):
        return _MathLib.ThreeTuple___eq__(self, p)

    def __ne__(self, p):
        return _MathLib.ThreeTuple___ne__(self, p)

    def printTuple(self):
        return _MathLib.ThreeTuple_printTuple(self)
ThreeTuple_swigregister = _MathLib.ThreeTuple_swigregister
ThreeTuple_swigregister(ThreeTuple)

class Vector3d(ThreeTuple):
    __swig_setmethods__ = {}
    for _s in [ThreeTuple]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Vector3d, name, value)
    __swig_getmethods__ = {}
    for _s in [ThreeTuple]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Vector3d, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _MathLib.new_Vector3d(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _MathLib.delete_Vector3d
    __del__ = lambda self: None

    def setToSum(self, a, b):
        return _MathLib.Vector3d_setToSum(self, a, b)

    def setToCrossProduct(self, a, b):
        return _MathLib.Vector3d_setToCrossProduct(self, a, b)

    def __add__(self, v):
        return _MathLib.Vector3d___add__(self, v)

    def setToDifference(self, a, b):
        return _MathLib.Vector3d_setToDifference(self, a, b)

    def __sub__(self, v):
        return _MathLib.Vector3d___sub__(self, v)

    def multiplyBy(self, n):
        return _MathLib.Vector3d_multiplyBy(self, n)

    def getOrthogonalVectors(self, a, b):
        return _MathLib.Vector3d_getOrthogonalVectors(self, a, b)

    def setToProduct(self, a, n):
        return _MathLib.Vector3d_setToProduct(self, a, n)

    def addScaledVector(self, a, s):
        return _MathLib.Vector3d_addScaledVector(self, a, s)

    def addVector(self, a):
        return _MathLib.Vector3d_addVector(self, a)

    def setToVectorBetween(self, a, b):
        return _MathLib.Vector3d_setToVectorBetween(self, a, b)

    def __mul__(self, n):
        return _MathLib.Vector3d___mul__(self, n)

    def __div__(self, n):
        return _MathLib.Vector3d___div__(self, n)

    def __iadd__(self, v):
        return _MathLib.Vector3d___iadd__(self, v)

    def __isub__(self, v):
        return _MathLib.Vector3d___isub__(self, v)

    def __imul__(self, n):
        return _MathLib.Vector3d___imul__(self, n)

    def __idiv__(self, n):
        return _MathLib.Vector3d___idiv__(self, n)

    def __neg__(self):
        return _MathLib.Vector3d___neg__(self)

    def dotProductWith(self, v):
        return _MathLib.Vector3d_dotProductWith(self, v)

    def crossProductWith(self, v):
        return _MathLib.Vector3d_crossProductWith(self, v)

    def length(self):
        return _MathLib.Vector3d_length(self)

    def projectionOn(self, v):
        return _MathLib.Vector3d_projectionOn(self, v)

    def angleWith(self, v):
        return _MathLib.Vector3d_angleWith(self, v)

    def toUnit(self):
        return _MathLib.Vector3d_toUnit(self)

    def unit(self):
        return _MathLib.Vector3d_unit(self)

    def isZeroVector(self):
        return _MathLib.Vector3d_isZeroVector(self)

    def setCrossProductMatrix(self, m):
        return _MathLib.Vector3d_setCrossProductMatrix(self, m)

    def rotate(self, alpha, axis):
        return _MathLib.Vector3d_rotate(self, alpha, axis)
Vector3d_swigregister = _MathLib.Vector3d_swigregister
Vector3d_swigregister(Vector3d)

class Point3d(ThreeTuple):
    __swig_setmethods__ = {}
    for _s in [ThreeTuple]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Point3d, name, value)
    __swig_getmethods__ = {}
    for _s in [ThreeTuple]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Point3d, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _MathLib.new_Point3d(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _MathLib.delete_Point3d
    __del__ = lambda self: None

    def setW(self, w):
        return _MathLib.Point3d_setW(self, w)

    def setToOffsetFromPoint(self, p, v, s):
        return _MathLib.Point3d_setToOffsetFromPoint(self, p, v, s)

    def __add__(self, v):
        return _MathLib.Point3d___add__(self, v)

    def __iadd__(self, v):
        return _MathLib.Point3d___iadd__(self, v)

    def __idiv__(self, val):
        return _MathLib.Point3d___idiv__(self, val)

    def __sub__(self, p):
        return _MathLib.Point3d___sub__(self, p)

    def __neg__(self):
        return _MathLib.Point3d___neg__(self)

    def __mul__(self, n):
        return _MathLib.Point3d___mul__(self, n)

    def drawObject(self):
        return _MathLib.Point3d_drawObject(self)
Point3d_swigregister = _MathLib.Point3d_swigregister
Point3d_swigregister(Point3d)

class Quaternion(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Quaternion, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Quaternion, name)
    __repr__ = _swig_repr
    __swig_setmethods__["s"] = _MathLib.Quaternion_s_set
    __swig_getmethods__["s"] = _MathLib.Quaternion_s_get
    if _newclass:
        s = _swig_property(_MathLib.Quaternion_s_get, _MathLib.Quaternion_s_set)
    __swig_setmethods__["v"] = _MathLib.Quaternion_v_set
    __swig_getmethods__["v"] = _MathLib.Quaternion_v_get
    if _newclass:
        v = _swig_property(_MathLib.Quaternion_v_get, _MathLib.Quaternion_v_set)

    def __init__(self, *args):
        this = _MathLib.new_Quaternion(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def setToProductOf(self, a, b, invA=False, invB=False):
        return _MathLib.Quaternion_setToProductOf(self, a, b, invA, invB)

    def getRotationAngle(self, positiveRotAxis):
        return _MathLib.Quaternion_getRotationAngle(self, positiveRotAxis)
    __swig_destroy__ = _MathLib.delete_Quaternion
    __del__ = lambda self: None

    def getAngle(self):
        return _MathLib.Quaternion_getAngle(self)

    def getAxis(self):
        return _MathLib.Quaternion_getAxis(self)

    def getComplexConjugate(self):
        return _MathLib.Quaternion_getComplexConjugate(self)

    def getInverse(self):
        return _MathLib.Quaternion_getInverse(self)

    def getLength(self):
        return _MathLib.Quaternion_getLength(self)

    def dotProductWith(self, other):
        return _MathLib.Quaternion_dotProductWith(self, other)

    def linearlyInterpolateWith(self, other, t):
        return _MathLib.Quaternion_linearlyInterpolateWith(self, other, t)

    def sphericallyInterpolateWith(self, other, t):
        return _MathLib.Quaternion_sphericallyInterpolateWith(self, other, t)
    __swig_getmethods__["getRotationQuaternion"] = lambda x: _MathLib.Quaternion_getRotationQuaternion
    if _newclass:
        getRotationQuaternion = staticmethod(_MathLib.Quaternion_getRotationQuaternion)

    def rotate(self, u):
        return _MathLib.Quaternion_rotate(self, u)

    def inverseRotate(self, u):
        return _MathLib.Quaternion_inverseRotate(self, u)

    def getRotationMatrix(self, *args):
        return _MathLib.Quaternion_getRotationMatrix(self, *args)

    def __imul__(self, *args):
        return _MathLib.Quaternion___imul__(self, *args)

    def __mul__(self, *args):
        return _MathLib.Quaternion___mul__(self, *args)

    def __add__(self, rhs):
        return _MathLib.Quaternion___add__(self, rhs)

    def __iadd__(self, rhs):
        return _MathLib.Quaternion___iadd__(self, rhs)

    def toUnit(self):
        return _MathLib.Quaternion_toUnit(self)

    def getS(self):
        return _MathLib.Quaternion_getS(self)

    def getV(self):
        return _MathLib.Quaternion_getV(self)

    def fastRotate(self, u, result):
        return _MathLib.Quaternion_fastRotate(self, u, result)

    def setToRotationQuaternion(self, angle, axis):
        return _MathLib.Quaternion_setToRotationQuaternion(self, angle, axis)

    def decomposeRotation(self, *args):
        return _MathLib.Quaternion_decomposeRotation(self, *args)
Quaternion_swigregister = _MathLib.Quaternion_swigregister
Quaternion_swigregister(Quaternion)

def Quaternion_getRotationQuaternion(angle, axis):
    return _MathLib.Quaternion_getRotationQuaternion(angle, axis)
Quaternion_getRotationQuaternion = _MathLib.Quaternion_getRotationQuaternion


def distanceBetweenOrientations(a, b):
    return _MathLib.distanceBetweenOrientations(a, b)
distanceBetweenOrientations = _MathLib.distanceBetweenOrientations
class Trajectory1d(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Trajectory1d, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Trajectory1d, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _MathLib.new_Trajectory1d(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _MathLib.delete_Trajectory1d
    __del__ = lambda self: None

    def evaluate_linear(self, t):
        return _MathLib.Trajectory1d_evaluate_linear(self, t)

    def evaluate_catmull_rom(self, t):
        return _MathLib.Trajectory1d_evaluate_catmull_rom(self, t)

    def getKnotValue(self, i):
        return _MathLib.Trajectory1d_getKnotValue(self, i)

    def getKnotPosition(self, i):
        return _MathLib.Trajectory1d_getKnotPosition(self, i)

    def setKnotValue(self, i, val):
        return _MathLib.Trajectory1d_setKnotValue(self, i, val)

    def setKnotPosition(self, i, pos):
        return _MathLib.Trajectory1d_setKnotPosition(self, i, pos)

    def getMinPosition(self):
        return _MathLib.Trajectory1d_getMinPosition(self)

    def getMaxPosition(self):
        return _MathLib.Trajectory1d_getMaxPosition(self)

    def getKnotCount(self):
        return _MathLib.Trajectory1d_getKnotCount(self)

    def addKnot(self, t, val):
        return _MathLib.Trajectory1d_addKnot(self, t, val)

    def removeKnot(self, i):
        return _MathLib.Trajectory1d_removeKnot(self, i)

    def clear(self):
        return _MathLib.Trajectory1d_clear(self)

    def simplify_catmull_rom(self, maxError, nbSamples=100):
        return _MathLib.Trajectory1d_simplify_catmull_rom(self, maxError, nbSamples)

    def copy(self, other):
        return _MathLib.Trajectory1d_copy(self, other)
Trajectory1d_swigregister = _MathLib.Trajectory1d_swigregister
Trajectory1d_swigregister(Trajectory1d)

class Trajectory3d(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Trajectory3d, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Trajectory3d, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _MathLib.new_Trajectory3d(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _MathLib.delete_Trajectory3d
    __del__ = lambda self: None

    def evaluate_linear(self, t):
        return _MathLib.Trajectory3d_evaluate_linear(self, t)

    def evaluate_catmull_rom(self, t):
        return _MathLib.Trajectory3d_evaluate_catmull_rom(self, t)

    def getKnotValue(self, i):
        return _MathLib.Trajectory3d_getKnotValue(self, i)

    def getKnotPosition(self, i):
        return _MathLib.Trajectory3d_getKnotPosition(self, i)

    def setKnotValue(self, i, val):
        return _MathLib.Trajectory3d_setKnotValue(self, i, val)

    def setKnotPosition(self, i, pos):
        return _MathLib.Trajectory3d_setKnotPosition(self, i, pos)

    def getMinPosition(self):
        return _MathLib.Trajectory3d_getMinPosition(self)

    def getMaxPosition(self):
        return _MathLib.Trajectory3d_getMaxPosition(self)

    def getKnotCount(self):
        return _MathLib.Trajectory3d_getKnotCount(self)

    def addKnot(self, t, val):
        return _MathLib.Trajectory3d_addKnot(self, t, val)

    def removeKnot(self, i):
        return _MathLib.Trajectory3d_removeKnot(self, i)

    def clear(self):
        return _MathLib.Trajectory3d_clear(self)

    def simplify_catmull_rom(self, maxError, nbSamples=100):
        return _MathLib.Trajectory3d_simplify_catmull_rom(self, maxError, nbSamples)

    def copy(self, other):
        return _MathLib.Trajectory3d_copy(self, other)
Trajectory3d_swigregister = _MathLib.Trajectory3d_swigregister
Trajectory3d_swigregister(Trajectory3d)

class Trajectory3dv(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Trajectory3dv, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Trajectory3dv, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _MathLib.new_Trajectory3dv(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _MathLib.delete_Trajectory3dv
    __del__ = lambda self: None

    def evaluate_linear(self, t):
        return _MathLib.Trajectory3dv_evaluate_linear(self, t)

    def evaluate_catmull_rom(self, t):
        return _MathLib.Trajectory3dv_evaluate_catmull_rom(self, t)

    def getKnotValue(self, i):
        return _MathLib.Trajectory3dv_getKnotValue(self, i)

    def getKnotPosition(self, i):
        return _MathLib.Trajectory3dv_getKnotPosition(self, i)

    def setKnotValue(self, i, val):
        return _MathLib.Trajectory3dv_setKnotValue(self, i, val)

    def setKnotPosition(self, i, pos):
        return _MathLib.Trajectory3dv_setKnotPosition(self, i, pos)

    def getMinPosition(self):
        return _MathLib.Trajectory3dv_getMinPosition(self)

    def getMaxPosition(self):
        return _MathLib.Trajectory3dv_getMaxPosition(self)

    def getKnotCount(self):
        return _MathLib.Trajectory3dv_getKnotCount(self)

    def addKnot(self, t, val):
        return _MathLib.Trajectory3dv_addKnot(self, t, val)

    def removeKnot(self, i):
        return _MathLib.Trajectory3dv_removeKnot(self, i)

    def clear(self):
        return _MathLib.Trajectory3dv_clear(self)

    def simplify_catmull_rom(self, maxError, nbSamples=100):
        return _MathLib.Trajectory3dv_simplify_catmull_rom(self, maxError, nbSamples)

    def copy(self, other):
        return _MathLib.Trajectory3dv_copy(self, other)
Trajectory3dv_swigregister = _MathLib.Trajectory3dv_swigregister
Trajectory3dv_swigregister(Trajectory3dv)

# This file is compatible with both classic and new-style classes.


