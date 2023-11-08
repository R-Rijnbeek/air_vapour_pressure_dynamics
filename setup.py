from setuptools import setup, find_packages
import re, io, os

class getPackageInfo:
    def __init__(self):
        self._package_module_name = None
        self._package_main_file = None
        self._git_config_file = None
        self._long_description = None
        self._description = None
        self._version = None
        self._author = None
        self._author_email = None
        self._git_host = None
        self._package_name = None
        self._git_issues_host = None
        self._required_packages = None
        self.__Process()
    
    def __Process(self):
        self.__getPackageModuleNameFromProject()
        self.__getPacketInitFileContent()
        self.__getconfigGIT()
        self.__getLongDescription()
        self.__getDescription()
        self.__getVersion()
        self.__getAuthor()
        self.__getAuthorEmail()
        self.__getGITHost()
        self.__getPackageName()
        self.__getGITIssuesHost()
        self.__getRequiredPackageList()

    def __getRequiredPackageList(self):
        dependencies =[]
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            lines = fh.readlines()
            for line in lines:
                cleanline = re.sub('\s+', '', line)
                if (not cleanline == ""):
                    dependencies.append(re.sub('\s+', '', line))
        self._required_packages = dependencies
        return True

    def __getPackageModuleNameFromProject(self):
        for dir in next(os.walk(".\src"))[1]:
            if not ".egg-info" in str(dir):
                self._package_module_name = dir
                return True

    def __getLongDescription(self):
        with open("README.md", "r", encoding="utf-8") as fh:
            self._long_description = fh.read()
            return  True

    def __getPacketInitFileContent(self):
        self._package_main_file = io.open(
                os.path.join('src', self._package_module_name,'__init__.py'),
                encoding='utf_8_sig'
            ).read()
        return True

    def __getconfigGIT(self):
        with open(os.path.join(os.getcwd(), '.git', 'config'), "r", encoding="utf-8") as fh:
            self._git_config_file = fh.read()
            return  True

    def __getDescription(self):
        self._description = re.search(
                r'(?<=\"\"\")((.|\n)*)(?=\"\"\")', 
                self._package_main_file
            ).group(1)
        return True

    def __getVersion(self):
        self._version = re.search(
            r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
            self._package_main_file
        ).group(1)
        return True

    def __getAuthor(self):
        self._author = re.search(
            r'__author__\s*=\s*[\'"]([^\'"]*)[\'"]',
            self._package_main_file
        ).group(1)
        return True
    
    def __getAuthorEmail(self):
        self._author_email = re.search(
                r'__email__\s*=\s*[\'"]([^\'"]*)[\'"]',
                self._package_main_file
            ).group(1)
        return True

    def __getGITHost(self):
        self._git_host = re.search(
                r'(?<=\[remote "origin"\]\n\turl = )((.|\n)*)(?=\.git)',
                self._git_config_file
            ).group(1)
        return True

    def __getGITIssuesHost(self):
        self._git_issues_host = self._git_host + "/issues"
        return True

    def __getPackageName(self):
        self._package_name = self._git_host.rsplit('/', 1)[-1]
        return True

    @property
    def package_name(self):
        return self._package_name

    @property
    def long_description(self):
        return self._long_description

    @property
    def description(self):
        return self._description

    @property
    def version(self):
        return self._version

    @property
    def author(self):
        return self._author

    @property
    def author_email(self):
        return self._author_email

    @property
    def git_host(self):
        return self._git_host

    @property
    def git_issues_host(self):
        return self._git_issues_host

    @property
    def required_packages(self):
        return self._required_packages


PACKAGE_INFO = getPackageInfo()

setup(
    name = PACKAGE_INFO.package_name,
    version = PACKAGE_INFO.version,
    author = PACKAGE_INFO.author ,
    author_email = PACKAGE_INFO.author_email ,
    description = PACKAGE_INFO.description,
    long_description = PACKAGE_INFO.long_description,
    long_description_content_type = "text/markdown",
    url = PACKAGE_INFO.git_host,
    project_urls = {
        "Bug Tracker": PACKAGE_INFO.git_issues_host,
    },
    data_files=[
        (
            '.git.',
            ['.git/config']
        ),
        (
            '.',
            ["requirements.txt"]
            )
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = { "": "src"},
    packages = find_packages(where = "src"),
    python_requires = ">=3.10",
    install_requires=PACKAGE_INFO.required_packages
)