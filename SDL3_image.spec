%define major 0
%define api 2.0
%define libname %mklibname %{name}
%define devname %mklibname %{name} -d

Summary:	Simple DirectMedia Layer 3 - image
Name:		SDL3_image
Version:	3.3.4
Release:	1
License:	Zlib
Group:		System/Libraries
Url:		https://www.libsdl.org/projects/SDL_image/index.html
Source0:	https://github.com/libsdl-org/SDL_image/releases/download/release-%{version}/SDL3_image-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:	make
BuildRequires:	pkgconfig(libavif)
BuildRequires:	pkgconfig(libjxl)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(sdl3)

%description
This is a simple library to load images of various formats as SDL2 surfaces.
This library currently supports BMP, PPM, PCX, GIF, JPEG, and PNG formats.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%files -n %{libname}
#{_libdir}/lib%{name}-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%files -n %{devname}
%doc CHANGES.txt
#{_includedir}/SDL2/*
#{_libdir}/lib%{name}.so
#{_libdir}/pkgconfig/SDL2_image.pc
#{_libdir}/cmake/SDL2_image/

#----------------------------------------------------------------------------

%prep
%autosetup -p1
rm -rf external/
touch NEWS README AUTHORS ChangeLog

%build
	
%cmake \
  -DSDLIMAGE_AVIF=ON \
  -DSDLIMAGE_AVIF_SAVE=ON \
  -DSDLIMAGE_AVIF_SHARED=ON \
  -DSDLIMAGE_BACKEND_STB=ON \
  -DSDLIMAGE_BMP=ON \
  -DSDLIMAGE_DEPS_SHARED=ON \
  -DSDLIMAGE_GIF=ON \
  -DSDLIMAGE_INSTALL=ON \
  -DSDLIMAGE_INSTALL_CPACK=ON \
  -DSDLIMAGE_INSTALL_MAN=ON \
  -DSDLIMAGE_JPG=ON \
  -DSDLIMAGE_JPG_SAVE=ON \
  -DSDLIMAGE_JXL=ON \
  -DSDLIMAGE_LBM=ON \
  -DSDLIMAGE_PCX=ON \
  -DSDLIMAGE_PNG=ON \
  -DSDLIMAGE_PNG_SAVE=ON \
  -DSDLIMAGE_PNM=ON \
  -DSDLIMAGE_QOI=ON \
  -DSDLIMAGE_SAMPLES=ON \
  -DSDLIMAGE_SAMPLES_INSTALL=ON \
  -DSDLIMAGE_STRICT=OFF \
  -DSDLIMAGE_SVG=ON \
  -DSDLIMAGE_TESTS=ON \
  -DSDLIMAGE_TESTS_INSTALL=ON \
  -DSDLIMAGE_TGA=ON \
  -DSDLIMAGE_TIF=ON \
  -DSDLIMAGE_TIF_SHARED=ON \
  -DSDLIMAGE_VENDORED=OFF \
  -DSDLIMAGE_WEBP=ON \
  -DSDLIMAGE_WEBP_SHARED=ON \
  -DSDLIMAGE_WERROR=OFF \
  -DSDLIMAGE_XCF=ON \
  -DSDLIMAGE_XPM=ON \
  -DSDLIMAGE_XV=ON
%make_build

%install
%make_install -C build
