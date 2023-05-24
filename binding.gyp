{
  "targets": [
    {
      "target_name": "exiv2node",
      "sources": ["exiv2node.cc"],
      "include_dirs": [
        "<!(node -p \"require('node-addon-api').include\")",
        "<!(pkg-config --cflags exiv2)"
      ],
      "libraries": ["<!(pkg-config --libs exiv2)"],
      "cflags_cc": [
        "-std=c++11",
        "-stdlib=libc++",
        "-fexceptions",
        "-frtti"
      ],
      "xcode_settings": {
        "MACOSX_DEPLOYMENT_TARGET": "10.7",
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "CLANG_CXX_LIBRARY": "libc++"
      },
      "msvs_settings": {
        "VCCLCompilerTool": {
          "ExceptionHandling": 1,
          "RuntimeLibrary": 3
        }
      }
    }
  ]
}