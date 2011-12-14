# -*- coding:utf-8 -*-
import copy

from templer.core.base import BaseTemplate

from templer.core.vars import StringVar

from templer.core.vars import EASY
from templer.core.vars import EXPERT

from sc.templer.core import DEFAULTS as D
from sc.templer.core.utils import gen_version
from sc.templer.core.utils import year


class ProjectDocumentation(BaseTemplate):

    summary = "Create a Sphinx Documentation for a project."
    help = """This template creates a documentation for a project following
              Simples Consultoria's standards.
           """

    category = "Simples Consultoria - Documentation"

    ndots = 0
    use_cheetah = True

    required_templates = []
    default_required_structures = ['sphinx_base', ]
    _template_dir = "templates/project_docs"

    vars = copy.deepcopy(BaseTemplate.vars)
    vars += [
        StringVar(
            'title',
            title='Project Title',
            description="""Inform the Project title. It could be something
                           like: Vogon Poetry Co. Intranet
                        """,
            default='Customer Project',
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""Title for this project."""),

        StringVar(
            'description',
            title='Description',
            description='One-line description of the project',
            default='Project developed by Simples Consultoria',
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""Description of this documentation."""),

        StringVar(
            'version',
            title='Version',
            description='Version number for project',
            modes=(EASY, EXPERT),
            default=gen_version(show_minor=False),
            page='Metadata',
            help="""Version number"""),

        StringVar(
            'author',
            title='Author',
            description='Name of author for project',
            default= D.get('author'),
            modes=(),
            page='Metadata',
            help="""Name that will appear on the theme description"""),

        StringVar(
            'author_email',
            title='Author Email',
            description='Email of author for project',
            default = D.get('email'),
            modes=(),
            page='Metadata',
            help="""Email of the author of the documentation."""),

        StringVar(
            'language',
            title='Language',
            description='Documentation Language',
            modes=(EXPERT, ),
            default='pt_BR',
            page='Metadata',
            help="""What is the language for this documentation?"""),
    ]

    def check_vars(self, vars, cmd):
        resp = super(ProjectDocumentation, self).check_vars(vars, cmd)
        resp['year'] = year()
        return resp


class InfraDocumentation(ProjectDocumentation):

    summary = "Create a Sphinx Documentation for a infrastructure project."
    help = """This template creates a documentation for a infrastructure
              following Simples Consultoria's standards.
           """

    _template_dir = "templates/infra_docs"
