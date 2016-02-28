#include <iostream>
#include <list>
#include <unordered_map>
#include <random>
#include <vector>

using namespace std;
class LRUCache {
public:
	LRUCache(int capacity) {
		data = unordered_map<int, pair<int, list<int>::iterator> >(capacity);
		max_size = capacity;
		size = 0;
		time_list = list<int>();
	}

	int get(int key) {
		auto ptr = data.find(key);
		if (ptr == data.end())
		{
			return -1;
		}
		else
		{
			int value = ptr->second.first;
			time_list.erase(ptr->second.second);
			time_list.push_front(key);
			data[key] = make_pair(value, time_list.begin());
			return value;
		}
	}

	void set(int key, int value) {
		if (data.find(key) != data.end())
		{
			time_list.erase(data[key].second);
			time_list.push_front(key);
			data[key] = make_pair(value, time_list.begin());
			return;
		}
		if (size != max_size)
		{
			time_list.push_front(key);
			data[key] = make_pair(value, time_list.begin());
			size++;
		}
		else
		{
			int last_key = time_list.back();
			time_list.pop_back();
			time_list.push_front(key);
			data.erase(last_key);
			data[key] = make_pair(value, time_list.begin());
		}
	}
private:
	unordered_map<int, pair<int, list<int>::iterator> > data;
	int size;
	int max_size;
	list<int> time_list;
};

int main() {
	auto lruCache = LRUCache(1);
	vector<int> keyset;
	lruCache.set(2, 1);
	cout << lruCache.get(2) << endl;
	lruCache.set(3,2);
	cout << lruCache.get(2) << endl;
	cout << lruCache.get(3) << endl;
	system("pause");
	return 0;
}