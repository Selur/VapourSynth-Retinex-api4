project('Retinex', 'cpp',
  default_options : ['buildtype=release', 'b_ndebug=if-release', 'cpp_std=c++14'],
  meson_version : '>=0.51.0',
  version : '5'
)

sources = [
  'source/Gaussian.cpp',
  'source/MSR.cpp',
  'source/MSRCP.cpp',
  'source/MSRCR.cpp',
  'source/VSPlugin.cpp'
]

vapoursynth_dep = dependency('vapoursynth', version : '>=55').partial_dependency(compile_args : true, includes : true)

if host_machine.cpu_family().startswith('x86') and meson.get_compiler('cpp').get_argument_syntax() == 'gcc'
  add_project_arguments('-mfpmath=sse', '-msse2', language : 'cpp')
endif

shared_module('retinex', sources,
  dependencies : vapoursynth_dep,
  include_directories : include_directories('include'),
  install : true,
  install_dir : join_paths(vapoursynth_dep.get_variable(pkgconfig : 'libdir', default_value : join_paths(get_option('prefix'), get_option('libdir'))), 'vapoursynth'),
  gnu_symbol_visibility : 'hidden'
)
