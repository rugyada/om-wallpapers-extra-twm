Summary:	Collection of wallpapers provided by OpenMandriva users
Name:		om-wallpapers-extra-twm
Version:	1
Release:	0
License:	GPL
Group:		Graphics
#Url:		https://www.openmandriva.org
Url:		https://github.com/rugyada/om-wallpapers-extra-twm
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

%description
Collection of wallpapers provided by OpenMandriva users for Tiling Window Manager

%files
%dir %{_datadir}/wallpapers/om-wallpapers-extra-twm/
%{_datadir}/wallpapers/om-wallpapers-extra-twm/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}%{_datadir}/wallpapers/om-wallpapers-extra-twm
cp * %{buildroot}%{_datadir}/wallpapers/om-wallpapers-extra-twm/
