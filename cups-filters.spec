Name:           cups-filters
Version:        1.28.16
Release:        3%{?dist}
# Rawhide no longer ships qpdf-devel; disable qpdf support entirely
%global _without_qpdf 1
Summary:        OpenPrinting CUPS Filters and backends
License:        GPLv2+
URL:            https://github.com/OpenPrinting/cups-filters
Source0:        https://www.openprinting.org/download/cups-filters/cups-filters-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf automake libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  ghostscript-devel
Requires:       ghostscript

%description
This is the legacy 1.28.x branch of cups-filters needed for older GDI/legacy printers.
It provides filters and backends that were removed in newer releases.

%prep
%autosetup

%build
%configure --disable-static --without-qpdf --with-poppler-glib QPDF_CFLAGS= QPDF_LIBS=
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README.md
/usr/lib*/cups/filter/*
/usr/lib*/cups/backend/*
/usr/share/cups

%changelog
* Fri Nov 07 2025 Vinod Kumar <vinod@example.com> - 1.28.16-2
- Rebuild on COPR, disable qpdf support for Rawhide

* Fri Nov 07 2025 Vinod Kumar <vinod@example.com> - 1.28.16-3
