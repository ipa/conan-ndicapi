conan source . --source-folder=debug_build/source
conan install . --install-folder=debug_build\build -s build_type=Debug -s arch=x86_64
conan build . --source-folder=debug_build\source\ --build-folder=debug_build\build\
conan package . --source-folder=debug_build\source\ --build-folder=debug_build\build --package-folder=debug_build\package
conan export-pkg . ipa/testing --source-folder=debug_build\source\ --build-folder=debug_build\build\ --force
conan test test_package\ NDICAPI/1.6@ipa/testing -s build_type=Debug


conan source . --source-folder=release_build/source
conan install . --install-folder=release_build\build -s build_type=Release -s arch=x86_64
conan build . --source-folder=release_build\source\ --build-folder=release_build\build\
conan package . --source-folder=release_build\source\ --build-folder=release_build\build --package-folder=release_build\package
conan export-pkg . ipa/testing --source-folder=release_build\source\ --build-folder=release_build\build\ --force
conan test test_package\ NDICAPI/1.6@ipa/testing -s build_type=Release
