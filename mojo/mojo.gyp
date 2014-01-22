# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'target_defaults': {
    'conditions': [
      ['mojo_shell_debug_url != ""', {
        'defines': [
          'MOJO_SHELL_DEBUG=1',
          'MOJO_SHELL_DEBUG_URL="<(mojo_shell_debug_url)"',
         ],
      }],
    ],
  },
  'variables': {
    'chromium_code': 1,
    'mojo_shell_debug_url%': "",
  },
  'includes': [
    'mojo_apps.gypi',
    'mojo_examples.gypi',
    'mojo_public.gypi',
    'mojo_services.gypi',
  ],
  'targets': [
    {
      'target_name': 'mojo',
      'type': 'none',
      'dependencies': [
        'mojo_bindings',
        'mojo_compositor_app',
        'mojo_common_lib',
        'mojo_common_unittests',
        'mojo_js',
        'mojo_js_unittests',
        'mojo_public_test_support',
        'mojo_public_bindings_unittests',
        'mojo_public_environment_unittests',
        'mojo_public_system_perftests',
        'mojo_public_system_unittests',
        'mojo_public_utility_unittests',
        'mojo_sample_app',
        'mojo_shell',
        'mojo_shell_lib',
        'mojo_shell_unittests',
        'mojo_system',
        'mojo_system_impl',
        'mojo_system_unittests',
        'mojo_utility',
      ],
      'conditions': [
        ['use_aura==1', {
          'dependencies': [
            'mojo_aura_demo',
          ],
        }],
      ]
    },
    {
      'target_name': 'mojo_run_all_unittests',
      'type': 'static_library',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/base.gyp:test_support_base',
        '../testing/gtest.gyp:gtest',
        'mojo_system',
        'mojo_system_impl',
      ],
      'sources': [
        'common/test/run_all_unittests.cc',
      ],
    },
    {
      'target_name': 'mojo_run_all_perftests',
      'type': 'static_library',
      'dependencies': [
        '../base/base.gyp:test_support_base',
        'mojo_system',
        'mojo_system_impl',
      ],
      'sources': [
        'common/test/run_all_perftests.cc',
      ],
    },
    {
      'target_name': 'mojo_system_impl',
      'type': '<(component)',
      'dependencies': [
        'mojo_system',
        '../base/base.gyp:base',
      ],
      'defines': [
        'MOJO_SYSTEM_IMPL_IMPLEMENTATION',
      ],
      'sources': [
        'system/channel.cc',
        'system/channel.h',
        'system/constants.h',
        'system/core_impl.cc',
        'system/core_impl.h',
        'system/data_pipe.cc',
        'system/data_pipe.h',
        'system/data_pipe_consumer_dispatcher.cc',
        'system/data_pipe_consumer_dispatcher.h',
        'system/data_pipe_producer_dispatcher.cc',
        'system/data_pipe_producer_dispatcher.h',
        'system/dispatcher.cc',
        'system/dispatcher.h',
        'system/embedder/embedder.cc',
        'system/embedder/embedder.h',
        'system/embedder/platform_channel_pair.cc',
        'system/embedder/platform_channel_pair.h',
        'system/embedder/platform_channel_pair_posix.cc',
        'system/embedder/platform_handle.cc',
        'system/embedder/platform_handle.h',
        'system/embedder/scoped_platform_handle.h',
        'system/local_data_pipe.cc',
        'system/local_data_pipe.h',
        'system/local_message_pipe_endpoint.cc',
        'system/local_message_pipe_endpoint.h',
        'system/memory.cc',
        'system/memory.h',
        'system/message_in_transit.cc',
        'system/message_in_transit.h',
        'system/message_pipe.cc',
        'system/message_pipe.h',
        'system/message_pipe_dispatcher.cc',
        'system/message_pipe_dispatcher.h',
        'system/message_pipe_endpoint.cc',
        'system/message_pipe_endpoint.h',
        'system/proxy_message_pipe_endpoint.cc',
        'system/proxy_message_pipe_endpoint.h',
        'system/raw_channel.h',
        'system/raw_channel_posix.cc',
        'system/raw_channel_win.cc',
        'system/simple_dispatcher.cc',
        'system/simple_dispatcher.h',
        'system/waiter.cc',
        'system/waiter.h',
        'system/waiter_list.cc',
        'system/waiter_list.h',
        # Test-only code:
        # TODO(vtl): It's a little unfortunate that these end up in the same
        # component as non-test-only code. In the static build, this code should
        # hopefully be dead-stripped.
        'system/embedder/test_embedder.cc',
        'system/embedder/test_embedder.h',
      ],
    },
    {
      'target_name': 'mojo_system_unittests',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:run_all_unittests',
        '../testing/gtest.gyp:gtest',
        'mojo_common_test_support',
        'mojo_system',
        'mojo_system_impl',
      ],
      'sources': [
        'system/core_impl_unittest.cc',
        'system/core_test_base.cc',
        'system/core_test_base.h',
        'system/data_pipe_unittest.cc',
        'system/dispatcher_unittest.cc',
        'system/embedder/embedder_unittest.cc',
        'system/local_data_pipe_unittest.cc',
        'system/message_pipe_dispatcher_unittest.cc',
        'system/message_pipe_unittest.cc',
        'system/multiprocess_message_pipe_unittest.cc',
        'system/raw_channel_posix_unittest.cc',
        'system/remote_message_pipe_posix_unittest.cc',
        'system/simple_dispatcher_unittest.cc',
        'system/test_utils.cc',
        'system/test_utils.h',
        'system/waiter_list_unittest.cc',
        'system/waiter_test_utils.cc',
        'system/waiter_test_utils.h',
        'system/waiter_unittest.cc',
      ],
    },
    {
      'target_name': 'mojo_gles2_impl',
      'type': '<(component)',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        'mojo_gles2',
      ],
      'defines': [
        'MOJO_GLES2_IMPL_IMPLEMENTATION',
      ],
      'sources': [
        'gles2/gles2_impl_export.h',
        'gles2/gles2_support_impl.cc',
        'gles2/gles2_support_impl.h',
      ],
    },
    {
      'target_name': 'mojo_common_lib',
      'type': '<(component)',
      'defines': [
        'MOJO_COMMON_IMPLEMENTATION',
      ],
      'dependencies': [
        '../base/base.gyp:base',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        'mojo_system',
      ],
      'sources': [
        'common/common_type_converters.cc',
        'common/common_type_converters.h',
        'common/handle_watcher.cc',
        'common/handle_watcher.h',
        'common/message_pump_mojo.cc',
        'common/message_pump_mojo.h',
        'common/message_pump_mojo_handler.h',
      ],
      'conditions': [
        ['OS == "win"', {
          # TODO(jschuh): crbug.com/167187 fix size_t to int truncations.
          'msvs_disabled_warnings': [
            4267,
          ],
        }],
      ],
    },
    {
      'target_name': 'mojo_common_test_support',
      'type': 'static_library',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/base.gyp:test_support_base',
        '../testing/gtest.gyp:gtest',
        'mojo_system',
        'mojo_system_impl',
      ],
      'sources': [
        'common/test/multiprocess_test_base.cc',
        'common/test/multiprocess_test_base.h',
      ],
    },
    {
      'target_name': 'mojo_common_unittests',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:base',
        '../base/base.gyp:base_message_loop_tests',
        '../testing/gtest.gyp:gtest',
        'mojo_bindings',
        'mojo_environment_chromium',
        'mojo_common_lib',
        'mojo_common_test_support',
        'mojo_public_test_support',
        'mojo_run_all_unittests',
        'mojo_system',
        'mojo_system_impl',
      ],
      'sources': [
        'common/common_type_converters_unittest.cc',
        'common/handle_watcher_unittest.cc',
        'common/message_pump_mojo_unittest.cc',
        'common/test/multiprocess_test_base_unittest.cc',
      ],
      'conditions': [
        ['OS == "win"', {
          # TODO(jschuh): crbug.com/167187 fix size_t to int truncations.
          'msvs_disabled_warnings': [
            4267,
          ],
        }],
      ],
    },
    {
      'target_name': 'mojo_environment_chromium',
      'type': 'static_library',
      'dependencies': [
        'mojo_environment_chromium_impl',
      ],
      'sources': [
        'environment/default_async_waiter.cc',
        'environment/buffer_tls.cc',
        'environment/environment.cc',
      ],
      'include_dirs': [
        '..',
      ],
      'export_dependent_settings': [
        'mojo_environment_chromium_impl',
      ],
    },
    {
      'target_name': 'mojo_environment_chromium_impl',
      'type': '<(component)',
      'defines': [
        'MOJO_ENVIRONMENT_IMPL_IMPLEMENTATION',
      ],
      'dependencies': [
        '../base/base.gyp:base',
        '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        'mojo_common_lib'
      ],
      'sources': [
        'environment/default_async_waiter_impl.cc',
        'environment/default_async_waiter_impl.h',
        'environment/buffer_tls_impl.cc',
        'environment/buffer_tls_impl.h',
      ],
      'include_dirs': [
        '..',
      ],
    },
    {
      'target_name': 'mojo_shell_lib',
      'type': 'static_library',
      'dependencies': [
        '../base/base.gyp:base',
        '../net/net.gyp:net',
        '../url/url.gyp:url_lib',
        'mojo_gles2_impl',
        'mojo_shell_bindings',
        'mojo_system',
        'mojo_system_impl',
        'mojo_native_viewport_service',
      ],
      'sources': [
        'shell/context.cc',
        'shell/context.h',
        'shell/dynamic_service_loader.cc',
        'shell/dynamic_service_loader.h',
        'shell/init.cc',
        'shell/init.h',
        'shell/loader.cc',
        'shell/loader.h',
        'shell/network_delegate.cc',
        'shell/network_delegate.h',
        'shell/run.cc',
        'shell/run.h',
        'shell/service_manager.cc',
        'shell/service_manager.h',
        'shell/storage.cc',
        'shell/storage.h',
        'shell/switches.cc',
        'shell/switches.h',
        'shell/task_runners.cc',
        'shell/task_runners.h',
        'shell/url_request_context_getter.cc',
        'shell/url_request_context_getter.h',
      ],
      'conditions': [
        ['OS == "win"', {
          # TODO(jschuh): crbug.com/167187 fix size_t to int truncations.
          'msvs_disabled_warnings': [
            4267,
          ],
        }],
      ],
    },
    {
      'target_name': 'mojo_shell_bindings',
      'type': 'static_library',
      'sources': [
        'shell/shell.mojom',
      ],
      'includes': [ 'public/bindings/mojom_bindings_generator.gypi' ],
      'export_dependent_settings': [
        'mojo_bindings',
        'mojo_system',
      ],
    },
    {
      'target_name': 'mojo_shell',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:base',
        '../ui/gl/gl.gyp:gl',
        '../url/url.gyp:url_lib',
        'mojo_common_lib',
        'mojo_environment_chromium',
        'mojo_shell_lib',
        'mojo_system',
        'mojo_system_impl',
      ],
      'sources': [
        'shell/desktop/mojo_main.cc',
      ],
      'conditions': [
        ['OS == "win"', {
          # TODO(jschuh): crbug.com/167187 fix size_t to int truncations.
          'msvs_disabled_warnings': [
            4267,
          ],
        }],
      ],
    },
    {
      'target_name': 'mojo_shell_unittests',
      'type': 'executable',
      'dependencies': [
        '../base/base.gyp:base',
        '../testing/gtest.gyp:gtest',
        'mojo_common_lib',
        'mojo_environment_chromium',
        'mojo_run_all_unittests',
        'mojo_shell_lib',
      ],
      'includes': [ 'public/bindings/mojom_bindings_generator.gypi' ],
      'sources': [
        'shell/service_manager_unittest.cc',
        'shell/test.mojom',
      ],
    },
  ],
  'conditions': [
    ['OS=="android"', {
      'targets': [
        {
          'target_name': 'mojo_native_viewport_java',
          'type': 'none',
          'dependencies': [
            '../base/base.gyp:base_java',
          ],
          'variables': {
            'java_in_dir': '<(DEPTH)/mojo/services/native_viewport/android',
          },
          'includes': [ '../build/java.gypi' ],
        },
        {
          'target_name': 'mojo_java_set_jni_headers',
          'type': 'none',
          'variables': {
            'jni_gen_package': 'mojo',
            'jni_generator_ptr_type': 'long',
            'input_java_class': 'java/util/HashSet.class',
          },
          'includes': [ '../build/jar_file_jni_generator.gypi' ],
        },
        {
          'target_name': 'mojo_jni_headers',
          'type': 'none',
          'dependencies': [
            'mojo_java_set_jni_headers',
          ],
          'sources': [
            'services/native_viewport/android/src/org/chromium/mojo/NativeViewportAndroid.java',
            'shell/android/apk/src/org/chromium/mojo_shell_apk/MojoMain.java',
          ],
          'variables': {
            'jni_gen_package': 'mojo',
            'jni_generator_ptr_type': 'long',
         },
          'includes': [ '../build/jni_generator.gypi' ],
        },
        {
          'target_name': 'libmojo_shell',
          'type': 'shared_library',
          'dependencies': [
            '../base/base.gyp:base',
            '../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
            '../ui/gfx/gfx.gyp:gfx',
            '../ui/gfx/gfx.gyp:gfx_geometry',
            '../ui/gl/gl.gyp:gl',
            'mojo_common_lib',
            'mojo_environment_chromium',
            'mojo_jni_headers',
            'mojo_shell_bindings',
            'mojo_shell_lib',
          ],
          'sources': [
            'shell/android/library_loader.cc',
            'shell/android/mojo_main.cc',
            'shell/android/mojo_main.h',
          ],
        },
        {
          'target_name': 'mojo_shell_apk',
          'type': 'none',
          'dependencies': [
            '../base/base.gyp:base_java',
            '../net/net.gyp:net_java',
            'mojo_native_viewport_java',
            'libmojo_shell',
          ],
          'variables': {
            'apk_name': 'MojoShell',
            'java_in_dir': '<(DEPTH)/mojo/shell/android/apk',
            'resource_dir': '<(DEPTH)/mojo/shell/android/apk/res',
            'native_lib_target': 'libmojo_shell',
          },
          'includes': [ '../build/java_apk.gypi' ],
        }
      ],
    }],
  ],
}
