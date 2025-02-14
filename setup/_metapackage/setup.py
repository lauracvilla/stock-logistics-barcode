import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-oca-stock-logistics-barcode",
    description="Meta package for oca-stock-logistics-barcode Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-barcodes_generator_abstract',
        'odoo11-addon-barcodes_generator_lot',
        'odoo11-addon-barcodes_generator_partner',
        'odoo11-addon-barcodes_generator_picking',
        'odoo11-addon-barcodes_generator_product',
        'odoo11-addon-base_gs1_barcode',
        'odoo11-addon-product_multi_ean',
        'odoo11-addon-stock_barcodes',
        'odoo11-addon-stock_scanner',
        'odoo11-addon-stock_scanner_inventory',
        'odoo11-addon-stock_scanner_location_info',
        'odoo11-addon-stock_scanner_receipt',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
