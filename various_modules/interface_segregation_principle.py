"""
Maybe not so relevant in Python due to the possibility to use multiple inheritance...
"""

from abc import ABC, abstractmethod


class CloudHostingProvider(ABC):
    @abstractmethod
    def create_server(region):
        ...

    @abstractmethod
    def list_servers(region):
        ...


class CDNProvider(ABC):
    @abstractmethod
    def get_cdna_address():
        ...


class CloudStorageProvider(ABC):
    @abstractmethod
    def store_file(name):
        ...

    @abstractmethod
    def get_file(name):
        ...


class Amazon(CloudHostingProvider, CDNProvider, CloudStorageProvider):
    def store_file(self, name: str):
        print(f"Storing the file {name} in AWS...")

    def get_file(self, name: str):
        print(f"Getting the file {name} from AWS...")

    def create_server(self, region: str):
        print(f"Creating a new server in the following region: {region}...")

    def list_servers(self, region: str):
        print(f"List all servers available in {region}...")

    def get_cdna_address(self):
        print("AWS CDNA address: ...")


class Dropbox(CloudStorageProvider):
    def store_file(self, name: str):
        print(f"Storing the file {name} in Dropbox...")

    def get_file(self, name: str):
        print(f"Getting the file {name} from Dropbox...")


if __name__ == "__main__":
    amazon = Amazon()
    dropbox = Dropbox()
    amazon.get_file("Baba")
    dropbox.store_file("Baba")
