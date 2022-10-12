/*
 * <one line to give the program's name and a brief idea of what it does.>
 * Copyright (C) 2016  <copyright holder> <email>
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * 
 */

#ifndef AP_H
#define AP_H

#include "System.h"
#include <mutex>
// using namespace ORB_SLAM3;

namespace ORB_SLAM3
{

class Ap
{
public:
    Ap();
    Ap(const string &Bssid):mApPos(Eigen::Vector3f()),mBssid(Bssid){};
    Ap(const Eigen::Vector3f &Pos, const string &Bssid):mApPos(Pos),mBssid(Bssid){};

    // Copy constructor.
    Ap(const Ap &ap);

    void SetApPos(const Eigen::Vector3f &Pos);
    Eigen::Vector3f GetApPos();

    void SetBssid(const string &Bssid);
    string GetBssid();
    static std::mutex mApGlobalMutex;
protected:
    // Position in absolute coordinates
    Eigen::Vector3f mApPos;
    std::string mBssid;

    // Mutex
    std::mutex mMutexApPos;
// private:
};
}
#endif // AP_H
