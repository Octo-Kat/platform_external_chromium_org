# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'chromium_code': 1,
  },
  'targets': [
    {
      'target_name': 'message_center',
      'type': '<(component)',
      'dependencies': [
        '../../base/base.gyp:base',
        '../../base/base.gyp:base_i18n',
        '../../base/third_party/dynamic_annotations/dynamic_annotations.gyp:dynamic_annotations',
        '../../build/temp_gyp/googleurl.gyp:googleurl',
        '../../skia/skia.gyp:skia',
        '../base/strings/ui_strings.gyp:ui_strings',
        '../compositor/compositor.gyp:compositor',
        '../ui.gyp:ui',
        '../ui.gyp:ui_resources',
      ],
      'defines': [
        'MESSAGE_CENTER_IMPLEMENTATION',
      ],
      'sources': [
        'message_center.cc',
        'message_center.h',
        'message_center_constants.cc',
        'message_center_constants.h',
        'message_center_export.h',
        'message_center_switches.cc',
        'message_center_switches.h',
        'message_center_tray.cc',
        'message_center_tray.h',
        'message_center_tray_delegate.h',
        'message_center_util.cc',
        'message_center_util.h',
        'notification.cc',
        'notification.h',
        'notification_change_observer.h',
        'notification_list.cc',
        'notification_list.h',
        'notification_types.cc',
        'notification_types.h',
        'notifier_settings.cc',
        'notifier_settings.h',
        'views/message_bubble_base.cc',
        'views/message_bubble_base.h',
        'views/message_center_bubble.cc',
        'views/message_center_bubble.h',
        'views/message_popup_bubble.cc',
        'views/message_popup_bubble.h',
        'views/message_popup_collection.cc',
        'views/message_popup_collection.h',
        'views/message_simple_view.cc',
        'views/message_simple_view.h',
        'views/message_view.cc',
        'views/message_view.h',
        'views/notifier_settings_view.cc',
        'views/notifier_settings_view.h',
        'views/notification_view.cc',
        'views/notification_view.h',
      ],
      # TODO(jschuh): crbug.com/167187 fix size_t to int truncations.
      'msvs_disabled_warnings': [ 4267, ],
      'conditions': [
        ['toolkit_views==1', {
          'dependencies': [
            '../views/views.gyp:views',
          ],
        }, {
          'sources/': [
            ['exclude', 'views/'],
          ],
        }],
      ],
    },
    {
      'target_name': 'message_center_unittests',
      'type': 'executable',
      'dependencies': [
        '../../base/base.gyp:base',
        '../../base/base.gyp:run_all_unittests',
        '../../base/base.gyp:test_support_base',
        '../../skia/skia.gyp:skia',
        '../../testing/gtest.gyp:gtest',
        '../ui.gyp:ui',
        'message_center',
      ],
      'sources': [
        'message_center_tray_unittest.cc',
        'notification_list_unittest.cc',
      ],
    },
  ],
}