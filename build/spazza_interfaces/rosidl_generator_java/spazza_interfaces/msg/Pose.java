// generated from rosidl_generator_java/resource/msg.java.em
// with input from spazza_interfaces:msg/Pose.idl
// generated code does not contain a copyright notice

package spazza_interfaces.msg;
import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;
import org.ros2.rcljava.common.JNIUtils;
import org.ros2.rcljava.interfaces.MessageDefinition;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public final class Pose implements MessageDefinition {

  private static final Logger logger = LoggerFactory.getLogger(Pose.class);

  static {
    try {
      JNIUtils.loadTypesupport(Pose.class);
    } catch (UnsatisfiedLinkError ule) {
      logger.error("Native code library failed to load.\n" + ule);
      System.exit(1);
    }
  }

  public static native long getDestructor();
  public static native long getFromJavaConverter();
  public static native long getToJavaConverter();
  public static native long getTypeSupport();

  public long getDestructorInstance() {
    return Pose.getDestructor();
  }

  public long getFromJavaConverterInstance() {
    return Pose.getFromJavaConverter();
  }

  public long getToJavaConverterInstance() {
    return Pose.getToJavaConverter();
  }

  public long getTypeSupportInstance() {
    return Pose.getTypeSupport();
  }



  private short x;

  public Pose setX(final short x) {

    this.x = x;
    return this;
  }

  public short getX() {
    return this.x;
  }

  private short y;

  public Pose setY(final short y) {

    this.y = y;
    return this;
  }

  public short getY() {
    return this.y;
  }

  public int hashCode() {
    return new HashCodeBuilder(17, 37)
      .append(this.x)
      .append(this.y)
      .toHashCode();
  }

 public boolean equals(Object obj) {
   if (obj == null) { return false; }
   if (obj == this) { return true; }
   if (obj.getClass() != getClass()) {
     return false;
   }
   Pose rhs = (Pose) obj;
   return new EqualsBuilder()
                .append(this.x, rhs.x)
                .append(this.y, rhs.y)
                .isEquals();
  }
}
