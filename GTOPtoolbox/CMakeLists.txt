project(optimizer LANGUAGES CXX)
cmake_minimum_required(VERSION 3.22)

set(CMAKE_CXX_STANDARD 20)
list(APPEND flags "-O3")

set(COMMON_SOURCES
    Astro_Functions.cpp
    Lambert.cpp
    mga_dsm.cpp
    mga.cpp
    misc4Tandem.cpp
    Pl_Eph_An.cpp
    PowSwingByInv.cpp
    propagateKEP.cpp
    time2distance.cpp
    trajobjfuns.cpp
    ZeroFinder.cpp
)

add_library(common STATIC ${COMMON_SOURCES})
target_compile_options(common PRIVATE ${flags})

function(add_common_executable NAME MAIN_SOURCE)
    add_executable(${NAME} ${MAIN_SOURCE})
    target_link_libraries(${NAME} PRIVATE common)
    target_compile_options(${NAME} PRIVATE ${flags})
endfunction()

add_common_executable(cassini1Main cassini1Main.cpp)
add_common_executable(jupiter1Main jupiter1Main.cpp)
add_common_executable(jupiter2Main jupiter2Main.cpp)
