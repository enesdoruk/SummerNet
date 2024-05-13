import torch.utils.data as data
import json
import os
import re
from transformers import AutoTokenizer


        
class ELIFE(data.Dataset):
    def __init__(self, path, mode) -> None:
        
        self.path = path
        self.mode = mode 
        
        if not self._check_exists():
            raise RuntimeError('Dataset not found.')
        
        with open(os.path.join(self.path, f'{self.mode}.json'), 'r') as file:
            self.data = json.load(file)
            
        self.tokenizer = AutoTokenizer.from_pretrained("EleutherAI/pythia-70m")

                
        
    @staticmethod
    def preprocess(input):   
  
        pass
    
    def __getitem__(self, index):
        input = self.data[index]['sections']
        input.insert(0, self.data[index]['abstract']) 
        import pdb; pdb.set_trace()
        input = [' '.join(inp) for inp in input]
        input = ' '. join(input)
        input = self.preprocess(input)

        encoded = self.tokenizer(input)["input_ids"]                
        
        target = self.data[index]['summary']
        
        pass
    
    def __len__(self):
        return len(self.data)
    
    def _check_exists(self):
        return os.path.exists(os.path.join(self.path,
                                           f'{self.mode}.json'))
    
    
if __name__ == "__main__":
    path = "data/elife"
    mode = "train"
    data = ELIFE(path, mode)
    data.__getitem__(2)