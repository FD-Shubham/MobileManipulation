import hello_helpers.hello_misc as hm
import numpy as np

class MyNode(hm.HelloNode):
    def __init__(self):
        hm.HelloNode.__init__(self)

    def main(self):
        hm.HelloNode.main(self, 'my_node', 'my_node', wait_for_first_pointcloud=False)
        self.stow_the_robot()
        self.move_to_pose({'joint_arm': 0.5, 'joint_lift':1.0}, blocking=True)
        self.move_to_pose({'joint_wrist_yaw': np.radians(45)}, blocking=True)
        self.move_to_pose({'joint_wrist_roll': np.radians(45)}, blocking=True)
        self.move_to_pose({'joint_wrist_pitch': np.radians(45)}, blocking=True)
        self.move_to_pose({'joint_gripper_finger_right': np.radians(45)}, blocking=True)
        self.move_to_pose({'joint_gripper_finger_right': np.radians(0)}, blocking=True)
        self.move_to_pose({'joint_head_pan': np.radians(120)}, blocking=True)
        self.move_to_pose({'joint_head_tilt': np.radians(-90)}, blocking=True)
        self.stow_the_robot()
        self.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)
        self.move_to_pose({'rotate_mobile_base': np.radians(180)}, blocking=True)
        self.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)
        self.stow_the_robot()

node = MyNode()
node.main()
