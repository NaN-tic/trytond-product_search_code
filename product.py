# This file is part product_search_code module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['Template']
__metaclass__ = PoolMeta


class Template:
    __name__ = "product.template"

    @classmethod
    def search_rec_name(cls, name, clause):
        products = Pool().get('product.product').search([
                ('code',) + tuple(clause[1:])
                ], order=[])
        if products:
            return [('id', 'in', map(int, [product.template.id
                    for product in products]))]
        return [('name',) + tuple(clause[1:])]
