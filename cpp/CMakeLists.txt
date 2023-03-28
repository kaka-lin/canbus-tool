cmake_minimum_required(VERSION 3.10.2)

project(canbus-tool)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSION OFF)

# Find Qt location
list(APPEND CMAKE_PREFIX_PATH "/usr/local/qt5")

# Find includes in corresponding build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)
# Instruct CMake to run moc automatically when needed.
set(CMAKE_AUTOMOC ON)
# Instruct CMake to run rcc automatically when needed.
set(CMAKE_AUTORCC ON)

# Find Qt5 libraries
find_package(Qt5 REQUIRED COMPONENTS
    Core Qml Quick)

# Source files
FILE(GLOB_RECURSE SOURCE_FILES
    "${CMAKE_SOURCE_DIR}/src/*.cpp"
    "${CMAKE_SOURCE_DIR}/src/*.cc"
    "${CMAKE_SOURCE_DIR}/src/*.c"
)

# Qt resources
string(LENGTH  ${PROJECT_SOURCE_DIR} LENGTH_OF_PROJECT_SOURCE_DIR)
math(EXPR LENGTH_OF_ROOT_DIR "${LENGTH_OF_PROJECT_SOURCE_DIR} - 4")
string(SUBSTRING ${PROJECT_SOURCE_DIR} 0 ${LENGTH_OF_ROOT_DIR} ROOT_DIR)
message("ROOT_DIR= ${ROOT_DIR}")
FILE(GLOB_RECURSE RESOURCES
    "${ROOT_DIR}/frontend/*.qrc"
)

add_definitions(-DFLUID_LOCAL)
# Tell CMake to create the xxx executable
add_executable(${PROJECT_NAME} ${SOURCE_FILES} ${RESOURCES})

# Use module from Qt5
target_compile_definitions(${PROJECT_NAME} PRIVATE $<$<OR:$<CONFIG:Debug>,$<CONFIG:RelWithDebInfo>>:QT_QML_DEBUG>)
target_link_libraries(${PROJECT_NAME}
    Qt5::Core Qt5::Qml Qt5::Quick
)

install(TARGETS ${PROJECT_NAME} DESTINATION bin)
