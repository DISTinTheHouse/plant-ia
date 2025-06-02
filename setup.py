from setuptools import setup, find_packages

setup(
    name='plant-ia',
    version='0.1.0',
    author='Jesús Alberto Ibarra Morales',
    author_email='ufkwear@gmail.com',
    description='Librería en español para estructurar prompts dinámicos con IA',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Spanish',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    python_requires='>=3.6',
)
