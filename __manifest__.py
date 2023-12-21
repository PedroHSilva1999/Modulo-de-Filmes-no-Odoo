{
    'name': 'Movie Management',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Pedro Henrique',
    'description': """Um módulo para gerenciar informações de filmes.""",
    'data': [
        'views/movie_tree_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}