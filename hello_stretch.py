import time
import stretch_body.robot
robot = stretch_body.robot.Robot()
robot.startup()

robot.stow()
robot.push_command()

robot.arm.move_to(0.5)
robot.lift.move_to(1.0)
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('wrist_roll', 1.57)
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('wrist_pitch', 1.57)
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('wrist_yaw', 1.57)
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('stretch_gripper', -70)
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('stretch_gripper', 70)
robot.push_command()
robot.wait_command()

robot.head.move_to('head_pan', 1.57)
robot.push_command()
robot.wait_command()

robot.head.move_to('head_tilt', 1.57)
robot.push_command()
robot.wait_command()

robot.stow()

robot.base.translate_by(0.5)
robot.push_command()
robot.wait_command()

robot.base.rotate_by(3.14)
robot.push_command()
robot.wait_command()

robot.base.translate_by(0.5)
robot.push_command()
robot.wait_command()