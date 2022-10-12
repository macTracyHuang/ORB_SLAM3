#include "Ap.h"

#include<mutex>

namespace ORB_SLAM3
{

mutex Ap::mApGlobalMutex;

/** 
 * @brief 构造函数
 */


void Ap::SetApPos(const Eigen::Vector3f &Pos)
{
    unique_lock<mutex> lock2(mApGlobalMutex);
    unique_lock<mutex> lock(mMutexApPos);
    mApPos = Pos;
}

Eigen::Vector3f Ap::GetApPos()
{
    unique_lock<mutex> lock(mMutexApPos);
    return mApPos;
}

void Ap::SetBssid(const string &Bssid)
{
    unique_lock<mutex> lock2(mApGlobalMutex);
    mBssid = Bssid;
}

string Ap::GetBssid()
{
    return mBssid;
}

} //namespace ORB_SLAM