from setuptools import find_packages, setup

setup(
    name="chordpro_chord",
    packages=find_packages(include=["chordpro_chord"]),
    version="0.1.0",
    description="ChordPro chord parser library",
    author="AysimaK",
    license="MIT",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)
