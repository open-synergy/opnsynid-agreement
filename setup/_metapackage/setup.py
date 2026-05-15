import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-open-synergy-opnsynid-agreement",
    description="Meta package for open-synergy-opnsynid-agreement Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-agreement_core',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
