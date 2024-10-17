Name:		texlive-ndsu-thesis-2022
Version:	63881
Release:	2
Summary:	North Dakota State University disquisition class 2022
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ndsu-thesis-2022
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ndsu-thesis-2022.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ndsu-thesis-2022.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A class for generating disquisitions (MS and PhD - thesis,
dissertation, and paper), intended to be in compliance with
North Dakota State University requirements. Updated (2022)
North Dakota State University LaTeX thesis class features
several functionalities, including not limited to, numbered and
non-numbered versions, overall justification, document point
sizes, fonts options, SI units, show frames, URL breaking, long
tables, subfigures, multi-page figures, chapter styles,
subfiles, algorithm listing, BibTeX and BibLaTeX support,
individual chapter and whole document bibliography, natbib
citations, and clever references. The supplied simple and
extended samples illustrate these features and guide students
to use the class.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ndsu-thesis-2022
%doc %{_texmfdistdir}/doc/latex/ndsu-thesis-2022

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
