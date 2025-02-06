import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-repair",
    description="Meta package for sygel-technology-sy-repair Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-repair_order_mass_validate>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
