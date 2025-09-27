import React from 'react'
import logo from "./assets/logo1.png"
import logo2 from "./assets/logo2.png"
import logo3 from "./assets/Logo.png"
import logo4 from "./assets/home 2.png"
import logo5 from "./assets/17-transfer.png"
import logo6 from "./assets/user 3 1.png"
import logo7 from "./assets/economic-investment 1.png"
import logo8 from "./assets/credit-card 1.png"
import logo9 from "./assets/loan 1.png"
import logo10 from "./assets/service 1.png"
import logo11 from "./assets/econometrics 1.png"
import logo12 from "./assets/settings solid 1.png"
import logo13 from "./assets/magnifying-glass 1.png"
import logo14 from "./assets/Group417.png"
import logo15 from "./assets/logo15.png"
import logo16 from "./assets/MaskGroup.png"




export default function App1() {
  return (
    <div>
      <div class="flex gap-70">
        <div>
            <aside class="ml-15 mt-10"> 
                    <div class="flex flex-col gap-8">
                        <img src={logo3} alt="bankdash" class="w-[183px] [h-36px]"/>
                        <div class="flex gap-3 items-center">
                          <img src={logo4} alt="house" class="w-[24px] h-[24px]"/>
                          <h1 class="text-gray-400 text-[20px] font-[500]">Dashboard</h1>
                        </div>
                      <div class="flex gap-3 items-center">
                        <img src={logo5} alt="transfer" class="w-[24px] h-[24px]"/>
                        <h1 class="text-gray-400 text-[20px] font-[500]">Transactions</h1>
                      </div>
                      <div class="flex gap-3 items-center">
                        <img src={logo6} alt="acc" class="w-[24px] h-[24px]"/>
                        <h1 class="text-gray-400 text-[20px] font-[500]">Accounts</h1>
                      </div>
                      <div class="flex gap-3 items-center">
                        <img src={logo7} alt="invest" class="w-[24px] h-[24px]" />
                        <h1 class="text-gray-400 text-[20px] font-[500]">Investments</h1>
                      </div>
                      <div class="flex gap-3 items-center">
                        <img src={logo8} alt="credit card" class="w-[24px] h-[24px]"/>
                        <h1 class="text-gray-400 text-[20px] font-[500]">Credit Cards</h1>
                      </div>
                      <div class="flex gap-3 items-center">
                        <img src={logo9} alt="loans" class="w-[24px] h-[24px]"/>
                        <h1 class="text-gray-400 text-[20px] font-[500]">Loans</h1>
                      </div>
                      <div class="flex gap-3 items-center">
                        <img src={logo10} alt="services" class="w-[24px] h-[24px]"/>
                        <h1 class="text-gray-400 text-[20px] font-[500]">Services</h1>
                      </div>
                      <div class="flex gap-3 items-center">
                        <img src={logo11} alt="privilages" class="w-[24px] h-[24px]"/>
                        <h1 class="text-gray-400 text-[20px] font-[500]">My Privileges</h1>
                      </div>
                      <div class="flex gap-3 items-center">
                        <img src={logo12} alt="setting" class="w-[24px] h-[24px]"/>
                        <h1 class="text-blue-700 text-[20px] font-[500]">Setting</h1>
                      </div>
                    </div>
                  </aside>
        </div>
        <div class="mt-5">
          <div class="flex gap justify-between">
            <div>
              <h1 class="text-[25px] font-bold text-blue-900 mt-4">Settings</h1>
            </div>
            <div class='flex'>
              <div class="px-4 py-2 rounded-lg text-gray-500 w-120 ml-10 mt-5 flex gap-3 border-none bg-gray-100">
                <img src={logo13} alt="glass" class="w-[16px] h-[16px] mt-1.5"/>
                <p>Search for something</p>
              </div>
                <img src={logo14} alt="logo1" class="mt-5"/>
                <img src={logo15} alt="logo2" class="mt-5"/>
                <img src={logo16} alt="logo3" class="mt-5"/>
            </div>
          </div>
          <div class="w-[1200px] h-[850px] bg-gray-100 flex items-center justify-center mt-5">
          <div class="w-[1100px] h-[700px] bg-white mb-[100px] ml-[10px] rounded-[25px]">
                    <div class="flex w-150 justify-around mt-10">
                    <h1 class="text-blue-400">Edit Profile</h1>
                    <h1 class="text-indigo-800">Preferences</h1>
                    <h1 class="text-blue-400">Security</h1>
                    </div>
                    <div class="w-25 h-0.5 bg-indigo-800 ml-65 rounded-t-[1px]"></div>
                    <div class="flex justify-between w-175 ml-10 mt-10">
                      <h1>Currency</h1>
                      <h1>Time Zone</h1>
                    </div>
                    <div class="flex">
                      <div class="px-4 py-2 border border-gray-300 rounded-lg text-gray-500 w-120 ml-10 mt-5">
                          USD
                      </div>
                      <div class="px-4 py-2 border border-gray-300 rounded-lg text-gray-500 ml-45 mt-5 w-120">
                        (GMT-12:00) International Date Line West
                      </div>
                    </div>
                    <h1 class="mt-5 ml-10 text-xl">Notification</h1>
                    <div class="flex gap-5">
                      <img src={logo} alt="logo1" class="ml-10" />
                      <p class="mt-1">I send or recieve digita currency</p>
                    </div>
                    <div class="flex gap-5">
                      <img src={logo2} alt="logo2" class="ml-10" />
                      <p class="mt-1">I receive merchant order</p>
                    </div>
                    <div class="flex gap-5">
                      <img src={logo} alt="logo1" class="ml-10" />
                      <p class="mt-1">There are recommendation for my account</p>
                    </div>
                    <div class="flex justify-end mt-5 mr-7">
                      <button class="w-35 h-10 bg-blue-700 text-white rounded-xl">Save</button>
                    </div>
                   </div>
                  </div>
              </div>
        </div>
      </div>
  )
}
