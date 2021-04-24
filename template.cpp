/*------------------------------------------
    Author : Suyash Chavan
    Walchand College of Engineering, Sangli
--------------------------------------------*/
#pragma GCC optimization ("O3")
#pragma GCC optimization ("unroll-loops")
#pragma GCC target ("sse4")

#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define ll                          long long
#define ld                          long double
#define endl                        "\n"
#define Endl                        "\n"
#define pb                          push_back
#define mp                          make_pair
#define eb                          emplace_back
#define ff                          first
#define ss                          second
#define loop(i,a,b)                 for(ll i=a;i<b;i++)
#define rloop(i,a,b)                for(ll i=a;i>=b;i--)
#define fill(a,v)                   memset(a, v, sizeof a)
#define all(a)                      a.begin(), a.end()
#define rall(vec)                   vec.rbegin(),vec.rend()
#define sortv(a)                    sort(a.begin(),a.end())
#define set_bits(a)                 __builtin_popcount(a)
#define ordered_set                 tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
#define fast_map(mp)                mp.reserve(1024);\
                                    mp.max_load_factor(0.25)
#define fast_io                     ios_base::sync_with_stdio(false);\
                                    cin.tie(NULL)
#define file_in                     freopen("input.txt", "r", stdin)
#define file_out                    freopen("output.txt", "w", stdout)
#define PI                          3.1415926535897932384626
#define INF                         1e18
#define EPS                         1e-9
#define change                      show = !show

bool show = true;

const int fx[4][2] = {{0, 1}, {0, -1}, {1, 0}, { -1, 0}};
const int fxx[8][2] = {{0, 1}, {0, -1}, {1, 0}, { -1, 0}, {1, 1}, {1, -1}, { -1, 1}, { -1, -1}};

template <typename T1, typename T2>
inline std::ostream& operator << (std::ostream& os, const std::pair<T1, T2>& p)
{
    return os << "(" << p.first << ", " << p.second << ")";
}
template<typename T>
inline std::ostream &operator << (std::ostream & os, const std::vector<T>& v)
{
    bool first = true;
    if (show)
        os << "[";
    for (unsigned int i = 0; i < v.size(); i++)
    {
        if (!first)
        {
            if (show)
                os << ", ";
            else
                os << " ";
        }
        os << v[i];
        first = false;
    }
    if (show)
        return os << "]\n";
    else
        return os << "\n";
}
template<typename T>
inline std::ostream &operator << (std::ostream & os, const std::set<T>& v)
{
    bool first = true;
    os << "[";
    for (typename std::set<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
    {
        if (!first)
            os << ", ";
        os << *ii;
        first = false;
    }
    return os << "]";
}
template<typename T1, typename T2>
inline std::ostream &operator << (std::ostream & os, const std::map<T1, T2>& v)
{
    bool first = true;
    os << "[";
    for (typename std::map<T1, T2>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
    {
        if (!first)
            os << ", ";
        os << *ii ;
        first = false;
    }
    return os << "]";
}

/*--------------------------- CODE STARTS FROM HERE---------------------------*/

int solve()
{

    return 0;
}

int main()
{
    fast_io;

    ll t = 1;
    cin >> t;
    while (t--)
        solve();

    return 0;
}
