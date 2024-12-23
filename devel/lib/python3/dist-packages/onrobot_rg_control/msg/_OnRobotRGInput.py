# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from onrobot_rg_control/OnRobotRGInput.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class OnRobotRGInput(genpy.Message):
  _md5sum = "94435113a24b6809371af29f68843bdb"
  _type = "onrobot_rg_control/OnRobotRGInput"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# gFOF : Current fingertip offset in 1/10 millimeters. The value is a signed two's complement number.

uint16 gFOF

# gGWD : Current width between the gripper fingers in 1/10 millimeters.
#        The width is provided without any fingertip offset, as it is measured between the insides of the aluminum fingers.

uint16 gGWD

# gSTA : Current device status, which indicates the status of the gripper and its motion.
# Bit       - Name              - Description
# 0 (LSB)   - Busy              - High (1) when a motion is ongoing, low (0) when not. The gripper will only accept new commands when this flag is low.
# 1         - Grip detected     - High (1) when an internal- or external grip is detected.
# 2         - S1 pushed         - High (1) when safety switch 1 is pushed.
# 3         - S1 trigged        - High (1) when safety circuit 1 is activated. The gripper will not move while this flag is high.
# 4         - S2 pushed         - High (1) when safety switch 2 is pushed.
# 5         - S2 trigged        - High (1) when safety circuit 2 is activated. The gripper will not move while this flag is high.
# 6         - Safety error      - High (1) when on power on any of the safety switch is pushed.
# 7 - 15    - Reserved          - Not used.

uint8 gSTA

# gWDF : Current width between the gripper fingers in 1/10 millimeters.
#        The set fingertip offset is considered.

uint16 gWDF
"""
  __slots__ = ['gFOF','gGWD','gSTA','gWDF']
  _slot_types = ['uint16','uint16','uint8','uint16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       gFOF,gGWD,gSTA,gWDF

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(OnRobotRGInput, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.gFOF is None:
        self.gFOF = 0
      if self.gGWD is None:
        self.gGWD = 0
      if self.gSTA is None:
        self.gSTA = 0
      if self.gWDF is None:
        self.gWDF = 0
    else:
      self.gFOF = 0
      self.gGWD = 0
      self.gSTA = 0
      self.gWDF = 0

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
      buff.write(_get_struct_2HBH().pack(_x.gFOF, _x.gGWD, _x.gSTA, _x.gWDF))
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
      end = 0
      _x = self
      start = end
      end += 7
      (_x.gFOF, _x.gGWD, _x.gSTA, _x.gWDF,) = _get_struct_2HBH().unpack(str[start:end])
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
      buff.write(_get_struct_2HBH().pack(_x.gFOF, _x.gGWD, _x.gSTA, _x.gWDF))
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
      end = 0
      _x = self
      start = end
      end += 7
      (_x.gFOF, _x.gGWD, _x.gSTA, _x.gWDF,) = _get_struct_2HBH().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2HBH = None
def _get_struct_2HBH():
    global _struct_2HBH
    if _struct_2HBH is None:
        _struct_2HBH = struct.Struct("<2HBH")
    return _struct_2HBH
