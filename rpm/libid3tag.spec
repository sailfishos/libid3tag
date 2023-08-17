Name:           libid3tag
Version:        0.16.2
Release:        1
Summary:        ID3 tag manipulation library
License:        GPLv2+
URL:            https://codeberg.org/tenacityteam/libid3tag
Source:	        %{name}-%{version}.tar.gz
# Based on https://codeberg.org/tenacityteam/libid3tag/pulls/3
Patch0:         cmake-hook-genre.dat-and-gperf-files-generation.patch
Patch1:         Add_unversioned_so.patch
BuildRequires:  cmake
BuildRequires:  gperf
BuildRequires:  zlib-devel >= 1.1.4

%description
libid3tag is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
ID3 tag library development files.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%cmake
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING COPYRIGHT
%doc CHANGES CREDITS README TODO
%{_libdir}/libid3tag.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/id3tag.h
%{_libdir}/libid3tag.so
%{_libdir}/cmake/id3tag/
%{_libdir}/pkgconfig/id3tag.pc

