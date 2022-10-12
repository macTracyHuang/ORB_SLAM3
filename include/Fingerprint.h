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

#ifndef FINGERPRINT_H
#define FINGERPRINT_H

#include "System.h"
#include <mutex>
// using namespace ORB_SLAM3;

namespace ORB_SLAM3
{

class Fingerprint
{
public:
    Fingerprint():mvAp(), mvRssi(){};
    Fingerprint(const vector<Ap*> &ap, const vector<int> &rssi) :mvAp(ap), mvRssi(rssi){};
    // Copy constructor.
    Fingerprint(const Fingerprint &fp);
    vector<Ap*> mvAp;
    vector<int> mvRssi;
    static std::mutex mFingerprintGlobalMutex;
protected:
    // Mutex
    std::mutex mMutexFingerprint;
// private:
};
}
#endif // Fingerprint_H
