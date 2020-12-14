pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'wasp_companion')
gnome = import('gnome')

gnome.compile_resources('wasp-companion',
  'wasp_companion.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'wasp-companion.in',
  output: 'wasp-companion',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

wasp_companion_sources = [
  '__init__.py',
  'main.py',
  'window.py',
]

install_data(wasp_companion_sources, install_dir: moduledir)
