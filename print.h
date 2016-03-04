#pragma once
#include <iosfwd>
#ifndef __PRINT_H__
#define __PRINT_H__

template<typename T1, typename T2>
std::ostream& operator <<(std::ostream& os, const std::pair<T1, T2>& p)
{
	return os << '(' << p.first << ", " << p.second << ')';
}

template<typename T>
std::ostream& operator << (std::ostream& os, const std::vector<T>& v)
{
	os << "[";
	size_t len = v.size();
	for (size_t i = 0; i < len; i++)
	{
		if (i != 0) os << ", ";
		os << v[i];
	}
	os << "]";
	return os;
}

#endif // __PRINT_H__