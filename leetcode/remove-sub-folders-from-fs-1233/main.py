class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folders_set = set(folder)
        parents = set()

        for f in folder:
            f_arr = f.split('/')
            f_arr = f_arr[1:]
            
            parents.add(f)
            for i in range(len(f_arr)):
                fstr = "/" + "/".join(f_arr[:i])
                if fstr in folders_set:
                    parents.remove(f)
                    parents.add(fstr)
                    break
            
        return list(parents)
