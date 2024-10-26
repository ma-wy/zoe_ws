; Auto-generated. Do not edit!


(cl:in-package gelsight_mini_ros-msg)


;//! \htmlinclude tracking_msg.msg.html

(cl:defclass <tracking_msg> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (marker_x
    :reader marker_x
    :initarg :marker_x
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (marker_y
    :reader marker_y
    :initarg :marker_y
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (marker_displacement_x
    :reader marker_displacement_x
    :initarg :marker_displacement_x
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (marker_displacement_y
    :reader marker_displacement_y
    :initarg :marker_displacement_y
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass tracking_msg (<tracking_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <tracking_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'tracking_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gelsight_mini_ros-msg:<tracking_msg> is deprecated: use gelsight_mini_ros-msg:tracking_msg instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <tracking_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gelsight_mini_ros-msg:header-val is deprecated.  Use gelsight_mini_ros-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'marker_x-val :lambda-list '(m))
(cl:defmethod marker_x-val ((m <tracking_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gelsight_mini_ros-msg:marker_x-val is deprecated.  Use gelsight_mini_ros-msg:marker_x instead.")
  (marker_x m))

(cl:ensure-generic-function 'marker_y-val :lambda-list '(m))
(cl:defmethod marker_y-val ((m <tracking_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gelsight_mini_ros-msg:marker_y-val is deprecated.  Use gelsight_mini_ros-msg:marker_y instead.")
  (marker_y m))

(cl:ensure-generic-function 'marker_displacement_x-val :lambda-list '(m))
(cl:defmethod marker_displacement_x-val ((m <tracking_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gelsight_mini_ros-msg:marker_displacement_x-val is deprecated.  Use gelsight_mini_ros-msg:marker_displacement_x instead.")
  (marker_displacement_x m))

(cl:ensure-generic-function 'marker_displacement_y-val :lambda-list '(m))
(cl:defmethod marker_displacement_y-val ((m <tracking_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gelsight_mini_ros-msg:marker_displacement_y-val is deprecated.  Use gelsight_mini_ros-msg:marker_displacement_y instead.")
  (marker_displacement_y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <tracking_msg>) ostream)
  "Serializes a message object of type '<tracking_msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'marker_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'marker_x))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'marker_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'marker_y))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'marker_displacement_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'marker_displacement_x))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'marker_displacement_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'marker_displacement_y))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <tracking_msg>) istream)
  "Deserializes a message object of type '<tracking_msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'marker_x) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'marker_x)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'marker_y) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'marker_y)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'marker_displacement_x) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'marker_displacement_x)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'marker_displacement_y) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'marker_displacement_y)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<tracking_msg>)))
  "Returns string type for a message object of type '<tracking_msg>"
  "gelsight_mini_ros/tracking_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'tracking_msg)))
  "Returns string type for a message object of type 'tracking_msg"
  "gelsight_mini_ros/tracking_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<tracking_msg>)))
  "Returns md5sum for a message object of type '<tracking_msg>"
  "8b99f4a1ff1377c066f07003f01617ae")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'tracking_msg)))
  "Returns md5sum for a message object of type 'tracking_msg"
  "8b99f4a1ff1377c066f07003f01617ae")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<tracking_msg>)))
  "Returns full string definition for message of type '<tracking_msg>"
  (cl:format cl:nil "# timestamp~%Header header~%~%# position and displacement of markers~%float32[] marker_x~%float32[] marker_y~%float32[] marker_displacement_x~%float32[] marker_displacement_y~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'tracking_msg)))
  "Returns full string definition for message of type 'tracking_msg"
  (cl:format cl:nil "# timestamp~%Header header~%~%# position and displacement of markers~%float32[] marker_x~%float32[] marker_y~%float32[] marker_displacement_x~%float32[] marker_displacement_y~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <tracking_msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'marker_x) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'marker_y) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'marker_displacement_x) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'marker_displacement_y) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <tracking_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'tracking_msg
    (cl:cons ':header (header msg))
    (cl:cons ':marker_x (marker_x msg))
    (cl:cons ':marker_y (marker_y msg))
    (cl:cons ':marker_displacement_x (marker_displacement_x msg))
    (cl:cons ':marker_displacement_y (marker_displacement_y msg))
))
