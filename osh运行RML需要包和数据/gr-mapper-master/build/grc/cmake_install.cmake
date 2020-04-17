# Install script for directory: /home/tujiaqi/Desktop/grc/gr-mapper-master/grc

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gnuradio/grc/blocks" TYPE FILE FILES
    "/home/tujiaqi/Desktop/grc/gr-mapper-master/grc/mapper_mapper.xml"
    "/home/tujiaqi/Desktop/grc/gr-mapper-master/grc/mapper_demapper.xml"
    "/home/tujiaqi/Desktop/grc/gr-mapper-master/grc/mapper_demapper_soft.xml"
    "/home/tujiaqi/Desktop/grc/gr-mapper-master/grc/mapper_mapper_msg.xml"
    "/home/tujiaqi/Desktop/grc/gr-mapper-master/grc/mapper_demapper_msg.xml"
    "/home/tujiaqi/Desktop/grc/gr-mapper-master/grc/mapper_preamble_insert_bb.xml"
    "/home/tujiaqi/Desktop/grc/gr-mapper-master/grc/mapper_preamble_sync_cc.xml"
    "/home/tujiaqi/Desktop/grc/gr-mapper-master/grc/mapper_preamble_sync_demapper.xml"
    "/home/tujiaqi/Desktop/grc/gr-mapper-master/grc/mapper_preamble_sync_demapper_hard.xml"
    "/home/tujiaqi/Desktop/grc/gr-mapper-master/grc/mapper_preamble_strip.xml"
    "/home/tujiaqi/Desktop/grc/gr-mapper-master/grc/mapper_timeslot_demux.xml"
    "/home/tujiaqi/Desktop/grc/gr-mapper-master/grc/mapper_prbs_source_b.xml"
    "/home/tujiaqi/Desktop/grc/gr-mapper-master/grc/mapper_prbs_sink_b.xml"
    )
endif()

