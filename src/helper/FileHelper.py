import os
class FileHelper:

    RESOURCES_DIR = os.path.abspath(os.path.join("src","resources"))
    TEMPLATE_DIR = os.path.join(RESOURCES_DIR,"template")
    ASSET_DIR = os.path.join(RESOURCES_DIR,"asset")
    TEMPORARY_DIR = os.path.abspath("tmp")

    @staticmethod
    def getTemplateFilePath(filename : str) -> str:
        return os.path.join(FileHelper.TEMPLATE_DIR, filename)

    @staticmethod
    def getTmpFilePath(filename) -> str:
        return  os.path.join(FileHelper.TEMPORARY_DIR,filename)

    @staticmethod
    def getAssetFilePath(filename) -> str:
        return  os.path.join(FileHelper.ASSET_DIR,filename)

    @staticmethod
    def saveInTmp(filename, data) -> str:
        if not os.path.exists(FileHelper.TEMPORARY_DIR):
            os.makedirs(FileHelper.TEMPORARY_DIR)
        path = FileHelper.getTmpFilePath(filename)
        with open(path, 'w') as f:
            f.write(data)