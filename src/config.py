from os.path import join
import numpy as np

from . import PROJECT_ROOT

KP_NAMES = ["Nose",
            "Neck",
            "RShoulder",
            "RElbow",
            "RWrist",
            "LShoulder",
            "LElbow",
            "LWrist",
            "MidHip",
            "RHip",
            "RKnee",
            "RAnkle",
            "LHip",
            "LKnee",
            "LAnkle",
            "REye",
            "LEye",
            "REar",
            "LEar",
            "LBigToe",
            "LSmallToe",
            "LHeel",
            "RBigToe",
            "RSmallToe",
            "RHeel",
            "Background"]


class OpenPoseV2Config:

    def __init__(self):
        self.joint_threshold = 0.1
        self.connection_threshold = 0.05
        self.min_vis_parts = 8
        self.resize_method = 'bicubic'
        self.weights_path = join(PROJECT_ROOT, 'models', 'openpose_v2', 'openpose_body25_keras.h5')
        self.input_res = 368
        self.use_gaussian_filtering = True
        self.gaussian_kernel_sigma = 3


class PoseCorrectionConfig:

    def __init__(self):
        # pose_predictor_dir = join(project_root, 'models', 'pose_correction', 'lstm_mae_exp_linear')
        # self.weights_path = join(pose_predictor_dir, 'weights_2020-04-11_17:58:54.json')
        # self.model_path = join(pose_predictor_dir, 'model_2020-04-11_17:58:54.h5')
        # self.config_path = join(pose_predictor_dir, 'config_2020-04-11_17:58:54.json')

        # pose_predictor_dir = join(project_root, 'models', 'pose_correction', 'lstm_mae_linear_light')
        # self.weights_path = join(pose_predictor_dir, 'weights_2020-04-14_16:22:20.json')
        # self.model_path = join(pose_predictor_dir, 'model_2020-04-14_16:22:20.h5')
        # self.config_path = join(pose_predictor_dir, 'config_2020-04-14_16:22:20.json')

        pose_predictor_dir = join(PROJECT_ROOT, 'models', 'pose_correction', 'lstm_mae_linear_dropout')
        self.weights_path = join(pose_predictor_dir, 'weights_2020-04-14_17:31:37.json')
        self.model_path = join(pose_predictor_dir, 'model_2020-04-14_17:31:37.h5')
        self.config_path = join(pose_predictor_dir, 'config_2020-04-14_17:31:37.json')

        self.max_error_radius = 1  # A correct key-point is supposed to be in a filed of :
        # max_error_radius_* (|predicted_kp, latest_kps|)


class HyperConfig:

    def __init__(self):
        self.use_gpu = True
        self.gpu_device_number = 0
        self.pad_value = 128
        self.drawing_stick = 5
        self.scales = (0.8, 1.0, 1.2)
        self.error_th = 20  # in degrees
        self.kp_names = ["Nose",
                         "Neck",
                         "RShoulder",
                         "RElbow",
                         "RWrist",
                         "LShoulder",
                         "LElbow",
                         "LWrist",
                         "MidHip",
                         "RHip",
                         "RKnee",
                         "RAnkle",
                         "LHip",
                         "LKnee",
                         "LAnkle",
                         "REye",
                         "LEye",
                         "REar",
                         "LEar",
                         "LBigToe",
                         "LSmallToe",
                         "LHeel",
                         "RBigToe",
                         "RSmallToe",
                         "RHeel",
                         "Background"]
        self.kp_mapper = dict(zip(range(len(self.kp_names)), self.kp_names))
        self.connections = [[1, 8],
                            [1, 2],
                            [1, 5],
                            [2, 3],
                            [3, 4],
                            [5, 6],
                            [6, 7],
                            [8, 9],
                            [9, 10],
                            [10, 11],
                            [8, 12],
                            [12, 13],
                            [13, 14],
                            [1, 0],
                            [0, 15],
                            [15, 17],
                            [0, 16],
                            [16, 18],
                            # [2, 17],
                            # [5, 18],
                            [14, 19],
                            [19, 20],
                            [14, 21],
                            [11, 22],
                            [22, 23],
                            [11, 24]]
        self.map_paf_to_connections = [[0, 1],
                                       [14, 15],
                                       [22, 23],
                                       [16, 17],
                                       [18, 19],
                                       [24, 25],
                                       [26, 27],
                                       [6, 7],
                                       [2, 3],
                                       [4, 5],
                                       [8, 9],
                                       [10, 11],
                                       [12, 13],
                                       [30, 31],
                                       [32, 33],
                                       [36, 37],
                                       [34, 35],
                                       [38, 39],
                                       # [20, 21],
                                       # [28, 29],
                                       [40, 41],
                                       [42, 43],
                                       [44, 45],
                                       [46, 47],
                                       [48, 49],
                                       [50, 51]]

        self.colors = [[255, 0, 0], [255, 85, 0], [255, 170, 0],
                       [255, 255, 0], [170, 255, 0], [85, 255, 0],
                       [0, 255, 0], [0, 255, 85], [0, 255, 170],
                       [0, 255, 255], [0, 170, 255], [0, 85, 255],
                       [0, 0, 255], [85, 0, 255], [170, 0, 255],
                       [255, 0, 255], [255, 0, 170], [255, 0, 85],
                       [255, 170, 85], [255, 170, 170], [255, 170, 255],
                       [255, 85, 85], [255, 85, 170], [255, 85, 255],
                       [170, 170, 170]]


class FeatureExtractorConfig:

    def __init__(self):

        mapper = dict(zip(KP_NAMES, range(len(KP_NAMES))))
        # self.points_comb = np.array([[mapper['RShoulder'], mapper['RElbow'], mapper['RWrist']],
        #                              [mapper['LWrist'], mapper['LElbow'], mapper['LShoulder']],
        #                              [mapper['Neck'], mapper['RShoulder'], mapper['RHip']],
        #                              [mapper['LHip'], mapper['LShoulder'], mapper['Neck']],
        #                              [mapper['RHip'], mapper['RShoulder'], mapper['RElbow']],
        #                              [mapper['LElbow'], mapper['LShoulder'], mapper['LHip']],
        #                              [mapper['MidHip'], mapper['RHip'], mapper['RKnee']],
        #                              [mapper['LKnee'], mapper['LHip'], mapper['MidHip']],
        #                              [mapper['RHip'], mapper['RKnee'], mapper['RAnkle']],
        #                              [mapper['LAnkle'], mapper['LKnee'], mapper['LHip']],
        #                              [mapper['RBigToe'], mapper['RAnkle'], mapper['RKnee']],
        #                              [mapper['LKnee'], mapper['LAnkle'], mapper['LBigToe']],
        #                              [mapper['RShoulder'], mapper['Neck'], mapper['Nose']],
        #                              [mapper['Nose'], mapper['Neck'], mapper['LShoulder']]])
        self.points_comb_str = np.array([['RShoulder', 'RElbow', 'RWrist'],
                                         ['LShoulder', 'LElbow', 'LWrist'],
                                         ['Neck', 'RShoulder', 'RHip'],
                                         ['Neck', 'MidHip', 'RHip'],
                                         ['RHip', 'RShoulder', 'RElbow'],
                                         ['LHip', 'LShoulder', 'LElbow'],
                                         ['MidHip', 'RHip', 'RKnee'],
                                         ['MidHip', 'LHip', 'LKnee'],
                                         ['RHip', 'RKnee', 'RAnkle'],
                                         ['LHip', 'LKnee', 'LAnkle'],
                                         ['RBigToe', 'RAnkle', 'RKnee'],
                                         ['LBigToe', 'LAnkle', 'LKnee'],
                                         ['RShoulder', 'Neck', 'Nose'],
                                         ['LShoulder', 'Neck', 'Nose']])
        points_comb = list()
        for row in self.points_comb_str:
            points_comb.append([mapper[item] for item in row])
        self.points_comb = np.array(points_comb)
