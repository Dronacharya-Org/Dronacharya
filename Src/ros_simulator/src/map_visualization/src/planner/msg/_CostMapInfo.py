"""autogenerated by genpy from planner/CostMapInfo.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class CostMapInfo(genpy.Message):
  _md5sum = "0d5388256fb29241b79718b0b39a338c"
  _type = "planner/CostMapInfo"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32[] x
int32[] y
int32[] z
uint32[] cost
int32[3] map_size
int32[3] map_offset

"""
  __slots__ = ['x','y','z','cost','map_size','map_offset']
  _slot_types = ['int32[]','int32[]','int32[]','uint32[]','int32[3]','int32[3]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x,y,z,cost,map_size,map_offset

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CostMapInfo, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.x is None:
        self.x = []
      if self.y is None:
        self.y = []
      if self.z is None:
        self.z = []
      if self.cost is None:
        self.cost = []
      if self.map_size is None:
        self.map_size = [0,0,0]
      if self.map_offset is None:
        self.map_offset = [0,0,0]
    else:
      self.x = []
      self.y = []
      self.z = []
      self.cost = []
      self.map_size = [0,0,0]
      self.map_offset = [0,0,0]

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.x)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.x))
      length = len(self.y)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.y))
      length = len(self.z)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.z))
      length = len(self.cost)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.cost))
      buff.write(_struct_3i.pack(*self.map_size))
      buff.write(_struct_3i.pack(*self.map_offset))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.x = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.y = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.z = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.cost = struct.unpack(pattern, str[start:end])
      start = end
      end += 12
      self.map_size = _struct_3i.unpack(str[start:end])
      start = end
      end += 12
      self.map_offset = _struct_3i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.x)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.x.tostring())
      length = len(self.y)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.y.tostring())
      length = len(self.z)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.z.tostring())
      length = len(self.cost)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.cost.tostring())
      buff.write(self.map_size.tostring())
      buff.write(self.map_offset.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.x = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.y = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.z = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.cost = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 12
      self.map_size = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=3)
      start = end
      end += 12
      self.map_offset = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=3)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3i = struct.Struct("<3i")