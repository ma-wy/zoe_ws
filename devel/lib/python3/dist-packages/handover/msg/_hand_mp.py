# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from handover/hand_mp.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class hand_mp(genpy.Message):
  _md5sum = "c180baaf221b3c9ea1b674a724ca2e79"
  _type = "handover/hand_mp"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
std_msgs/String handedness
geometry_msgs/Point wrist
geometry_msgs/Point thumb_tip
geometry_msgs/Point index_tip
geometry_msgs/Point middle_tip
geometry_msgs/Point ring_tip
geometry_msgs/Point pinky_tip
geometry_msgs/Point index_mcp
geometry_msgs/Point middle_mcp
geometry_msgs/Point ring_mcp
geometry_msgs/Point pinky_mcp

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: std_msgs/String
string data

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
"""
  __slots__ = ['header','handedness','wrist','thumb_tip','index_tip','middle_tip','ring_tip','pinky_tip','index_mcp','middle_mcp','ring_mcp','pinky_mcp']
  _slot_types = ['std_msgs/Header','std_msgs/String','geometry_msgs/Point','geometry_msgs/Point','geometry_msgs/Point','geometry_msgs/Point','geometry_msgs/Point','geometry_msgs/Point','geometry_msgs/Point','geometry_msgs/Point','geometry_msgs/Point','geometry_msgs/Point']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,handedness,wrist,thumb_tip,index_tip,middle_tip,ring_tip,pinky_tip,index_mcp,middle_mcp,ring_mcp,pinky_mcp

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(hand_mp, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.handedness is None:
        self.handedness = std_msgs.msg.String()
      if self.wrist is None:
        self.wrist = geometry_msgs.msg.Point()
      if self.thumb_tip is None:
        self.thumb_tip = geometry_msgs.msg.Point()
      if self.index_tip is None:
        self.index_tip = geometry_msgs.msg.Point()
      if self.middle_tip is None:
        self.middle_tip = geometry_msgs.msg.Point()
      if self.ring_tip is None:
        self.ring_tip = geometry_msgs.msg.Point()
      if self.pinky_tip is None:
        self.pinky_tip = geometry_msgs.msg.Point()
      if self.index_mcp is None:
        self.index_mcp = geometry_msgs.msg.Point()
      if self.middle_mcp is None:
        self.middle_mcp = geometry_msgs.msg.Point()
      if self.ring_mcp is None:
        self.ring_mcp = geometry_msgs.msg.Point()
      if self.pinky_mcp is None:
        self.pinky_mcp = geometry_msgs.msg.Point()
    else:
      self.header = std_msgs.msg.Header()
      self.handedness = std_msgs.msg.String()
      self.wrist = geometry_msgs.msg.Point()
      self.thumb_tip = geometry_msgs.msg.Point()
      self.index_tip = geometry_msgs.msg.Point()
      self.middle_tip = geometry_msgs.msg.Point()
      self.ring_tip = geometry_msgs.msg.Point()
      self.pinky_tip = geometry_msgs.msg.Point()
      self.index_mcp = geometry_msgs.msg.Point()
      self.middle_mcp = geometry_msgs.msg.Point()
      self.ring_mcp = geometry_msgs.msg.Point()
      self.pinky_mcp = geometry_msgs.msg.Point()

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
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.handedness.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_30d().pack(_x.wrist.x, _x.wrist.y, _x.wrist.z, _x.thumb_tip.x, _x.thumb_tip.y, _x.thumb_tip.z, _x.index_tip.x, _x.index_tip.y, _x.index_tip.z, _x.middle_tip.x, _x.middle_tip.y, _x.middle_tip.z, _x.ring_tip.x, _x.ring_tip.y, _x.ring_tip.z, _x.pinky_tip.x, _x.pinky_tip.y, _x.pinky_tip.z, _x.index_mcp.x, _x.index_mcp.y, _x.index_mcp.z, _x.middle_mcp.x, _x.middle_mcp.y, _x.middle_mcp.z, _x.ring_mcp.x, _x.ring_mcp.y, _x.ring_mcp.z, _x.pinky_mcp.x, _x.pinky_mcp.y, _x.pinky_mcp.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.handedness is None:
        self.handedness = std_msgs.msg.String()
      if self.wrist is None:
        self.wrist = geometry_msgs.msg.Point()
      if self.thumb_tip is None:
        self.thumb_tip = geometry_msgs.msg.Point()
      if self.index_tip is None:
        self.index_tip = geometry_msgs.msg.Point()
      if self.middle_tip is None:
        self.middle_tip = geometry_msgs.msg.Point()
      if self.ring_tip is None:
        self.ring_tip = geometry_msgs.msg.Point()
      if self.pinky_tip is None:
        self.pinky_tip = geometry_msgs.msg.Point()
      if self.index_mcp is None:
        self.index_mcp = geometry_msgs.msg.Point()
      if self.middle_mcp is None:
        self.middle_mcp = geometry_msgs.msg.Point()
      if self.ring_mcp is None:
        self.ring_mcp = geometry_msgs.msg.Point()
      if self.pinky_mcp is None:
        self.pinky_mcp = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.handedness.data = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.handedness.data = str[start:end]
      _x = self
      start = end
      end += 240
      (_x.wrist.x, _x.wrist.y, _x.wrist.z, _x.thumb_tip.x, _x.thumb_tip.y, _x.thumb_tip.z, _x.index_tip.x, _x.index_tip.y, _x.index_tip.z, _x.middle_tip.x, _x.middle_tip.y, _x.middle_tip.z, _x.ring_tip.x, _x.ring_tip.y, _x.ring_tip.z, _x.pinky_tip.x, _x.pinky_tip.y, _x.pinky_tip.z, _x.index_mcp.x, _x.index_mcp.y, _x.index_mcp.z, _x.middle_mcp.x, _x.middle_mcp.y, _x.middle_mcp.z, _x.ring_mcp.x, _x.ring_mcp.y, _x.ring_mcp.z, _x.pinky_mcp.x, _x.pinky_mcp.y, _x.pinky_mcp.z,) = _get_struct_30d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.handedness.data
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_30d().pack(_x.wrist.x, _x.wrist.y, _x.wrist.z, _x.thumb_tip.x, _x.thumb_tip.y, _x.thumb_tip.z, _x.index_tip.x, _x.index_tip.y, _x.index_tip.z, _x.middle_tip.x, _x.middle_tip.y, _x.middle_tip.z, _x.ring_tip.x, _x.ring_tip.y, _x.ring_tip.z, _x.pinky_tip.x, _x.pinky_tip.y, _x.pinky_tip.z, _x.index_mcp.x, _x.index_mcp.y, _x.index_mcp.z, _x.middle_mcp.x, _x.middle_mcp.y, _x.middle_mcp.z, _x.ring_mcp.x, _x.ring_mcp.y, _x.ring_mcp.z, _x.pinky_mcp.x, _x.pinky_mcp.y, _x.pinky_mcp.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.handedness is None:
        self.handedness = std_msgs.msg.String()
      if self.wrist is None:
        self.wrist = geometry_msgs.msg.Point()
      if self.thumb_tip is None:
        self.thumb_tip = geometry_msgs.msg.Point()
      if self.index_tip is None:
        self.index_tip = geometry_msgs.msg.Point()
      if self.middle_tip is None:
        self.middle_tip = geometry_msgs.msg.Point()
      if self.ring_tip is None:
        self.ring_tip = geometry_msgs.msg.Point()
      if self.pinky_tip is None:
        self.pinky_tip = geometry_msgs.msg.Point()
      if self.index_mcp is None:
        self.index_mcp = geometry_msgs.msg.Point()
      if self.middle_mcp is None:
        self.middle_mcp = geometry_msgs.msg.Point()
      if self.ring_mcp is None:
        self.ring_mcp = geometry_msgs.msg.Point()
      if self.pinky_mcp is None:
        self.pinky_mcp = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.handedness.data = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.handedness.data = str[start:end]
      _x = self
      start = end
      end += 240
      (_x.wrist.x, _x.wrist.y, _x.wrist.z, _x.thumb_tip.x, _x.thumb_tip.y, _x.thumb_tip.z, _x.index_tip.x, _x.index_tip.y, _x.index_tip.z, _x.middle_tip.x, _x.middle_tip.y, _x.middle_tip.z, _x.ring_tip.x, _x.ring_tip.y, _x.ring_tip.z, _x.pinky_tip.x, _x.pinky_tip.y, _x.pinky_tip.z, _x.index_mcp.x, _x.index_mcp.y, _x.index_mcp.z, _x.middle_mcp.x, _x.middle_mcp.y, _x.middle_mcp.z, _x.ring_mcp.x, _x.ring_mcp.y, _x.ring_mcp.z, _x.pinky_mcp.x, _x.pinky_mcp.y, _x.pinky_mcp.z,) = _get_struct_30d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_30d = None
def _get_struct_30d():
    global _struct_30d
    if _struct_30d is None:
        _struct_30d = struct.Struct("<30d")
    return _struct_30d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
