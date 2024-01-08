import os
from .utils import DatasetBase
from .oxford_pets import OxfordPets

# template corresponds to tau func in the main model diagram in the paper
template = ['a photo of a {}, a type of component package.']


class Package19(DatasetBase):

    dataset_dir = 'package-19'

    def __init__(self, root, num_shots):
        self.dataset_dir = os.path.join(root, self.dataset_dir)
        self.image_dir = os.path.join(self.dataset_dir, 'data')
        self.split_path = os.path.join(
            self.dataset_dir, 'split_zhao_Package19.json')

        self.template = template

        train, val, test = OxfordPets.read_split(
            self.split_path, self.image_dir)
        train = self.generate_fewshot_dataset(train, num_shots=num_shots)

        super().__init__(train_x=train, val=val, test=test)
