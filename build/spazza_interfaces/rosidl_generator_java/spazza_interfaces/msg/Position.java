// generated from rosidl_generator_java/resource/msg.java.em
// with input from spazza_interfaces:msg/Position.idl
// generated code does not contain a copyright notice

package spazza_interfaces.msg;
import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;
import org.ros2.rcljava.common.JNIUtils;
import org.ros2.rcljava.interfaces.MessageDefinition;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public final class Position implements MessageDefinition {

  private static final Logger logger = LoggerFactory.getLogger(Position.class);

  static {
    try {
      JNIUtils.loadTypesupport(Position.class);
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
    return Position.getDestructor();
  }

  public long getFromJavaConverterInstance() {
    return Position.getFromJavaConverter();
  }

  public long getToJavaConverterInstance() {
    return Position.getToJavaConverter();
  }

  public long getTypeSupportInstance() {
    return Position.getTypeSupport();
  }



  private double x;

  public Position setX(final double x) {

    this.x = x;
    return this;
  }

  public double getX() {
    return this.x;
  }

  private double y;

  public Position setY(final double y) {

    this.y = y;
    return this;
  }

  public double getY() {
    return this.y;
  }

  private double z;

  public Position setZ(final double z) {

    this.z = z;
    return this;
  }

  public double getZ() {
    return this.z;
  }

  private double theta;

  public Position setTheta(final double theta) {

    this.theta = theta;
    return this;
  }

  public double getTheta() {
    return this.theta;
  }

  public int hashCode() {
    return new HashCodeBuilder(17, 37)
      .append(this.x)
      .append(this.y)
      .append(this.z)
      .append(this.theta)
      .toHashCode();
  }

 public boolean equals(Object obj) {
   if (obj == null) { return false; }
   if (obj == this) { return true; }
   if (obj.getClass() != getClass()) {
     return false;
   }
   Position rhs = (Position) obj;
   return new EqualsBuilder()
                .append(this.x, rhs.x)
                .append(this.y, rhs.y)
                .append(this.z, rhs.z)
                .append(this.theta, rhs.theta)
                .isEquals();
  }
}
