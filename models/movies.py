from datetime import datetime
from odoo import models, fields, api


class Movie(models.Model):
    _name = 'movie.management'
    _description = 'Informações sobre filmes'

    name = fields.Char(string='Nome', required=True)
    genre = fields.Char(string='Gênero')
    director = fields.Char(string='Diretor')
    actors = fields.Char(string='Atores')

    release_date = fields.Date(string='Data de Lançamento')
    age = fields.Integer(string='Idade do Filme', compute='_compute_movie_age')

    @api.depends('release_date')
    def _compute_movie_age(self):
        for movie in self:
            if movie.release_date:
                release_date = fields.Date.from_string(movie.release_date)
                today = datetime.now().date()
                movie.age = today.year - release_date.year - ((today.month, today.day) < (release_date.month, release_date.day))
            else:
                movie.age = 0