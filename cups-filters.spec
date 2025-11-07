Name:           cups-filters
Version:        1.28.16
Release:        1%{?dist}
Summary:        OpenPrinting CUPS Filters and backends
License:        GPLv2+
URL:            https://github.com/OpenPrinting/cups-filters
Source0:        https://www.openprinting.org/download/cups-filters/cups-filters-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf automake libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(qpdf)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  ghostscript-devel
Requires:       ghostscript

%description
This is the legacy 1.28.x branch of cups-filters needed for older GDI/legacy printers.
It provides filters and backends that were removed in newer releases.

%prep
%autosetup

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README.md
/usr/lib*/cups/filter/*
/usr/lib*/cups/backend/*
/usr/share/cups
