from setuptools import setup, find_packages

setup(
    name='vectoria',
    version='0.1',
    packages=find_packages(),  # Encuentra automáticamente los paquetes del proyecto
    include_package_data=True,  # Incluye archivos no Python definidos en MANIFEST.in
    install_requires=[          # Lista de dependencias del proyecto
        'requests',
        'numpy',
        'matplotlib',
    ],
    entry_points={              # Puntos de entrada para scripts o aplicaciones de consola
        'console_scripts': [
            'mi_script = mi_paquete.mimodulo:funcion_principal',
        ],
    },
    author='atp',
    author_email='adriatp94@gmail.com',
    description='Una descripción corta de tu proyecto',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tu_usuario/tu_proyecto',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)