Name:           libid3tag
Version:        0.15.1b
Release:        7
Summary:        ID3 tag manipulation library

Group:          System/Libraries
License:        GPLv2+
URL:            http://www.underbit.com/products/mad/
Source:			ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
Patch1:	0001-libid3tag-0.15.1b-fix_overflow.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  zlib-devel >= 1.1.4

%description
libid3tag is a library for reading and (eventually) writing ID3 tags,
both ID3v1 and the various versions of ID3v2.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
ID3 tag library development files.


%prep
%setup -q
%patch1 -p1

# *.pc originally from the Debian package.
cat << \EOF > %{name}.pc
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: id3tag
Description: ID3 tag manipulation library
Requires:
Version: %{version}
Libs: -L${libdir} -lid3tag
Cflags: -I${includedir}
EOF


%build
%configure --disable-dependency-tracking --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
install -Dpm 644 %{name}.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/id3tag.pc


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc CHANGES COPYING COPYRIGHT CREDITS README TODO
%{_libdir}/libid3tag.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/id3tag.h
%{_libdir}/libid3tag.so
%{_libdir}/pkgconfig/id3tag.pc

