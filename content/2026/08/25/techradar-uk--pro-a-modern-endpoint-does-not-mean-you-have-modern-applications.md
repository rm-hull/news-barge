---
title: A modern endpoint does not mean you have modern applications
source_url: https://www.techradar.com/pro/a-modern-endpoint-does-not-mean-you-have-modern-applications
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-25T16:51:12Z'
published: '2026-08-25T00:00:00Z'
description: Why application modernization must start before endpoint migration
image: https://cdn.mos.cms.futurecdn.net/KNPUc7wQaTTAwBR9EVypsK-2560-80.jpg
---

![An outline of a cloud in neon orange, inside a circle of blue fibers, suggesting cloud computing](https://cdn.mos.cms.futurecdn.net/KNPUc7wQaTTAwBR9EVypsK.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

There is a point in many endpoint projects when the new environment appears to be ready.

Devices are enrolled, policies are in place and physical endpoints and virtual desktops—including Cloud PCs—can be provisioned.

From an infrastructure perspective, most of the difficult work seems to have been done.

The applications often tell a different story.

CEO of appCURE.

Moving an older application onto a new platform does not alter its underlying behavior.

It may still rely on ageing components and expect administrator access to write files and registry entries across the device. Its update process may also be largely manual or poorly documented.

A well-managed endpoint is valuable, but it cannot make a difficult application easier to maintain simply by hosting it.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## A successful deployment can hide the real work

Modern management platforms have made it much quicker to enroll devices, assign software and apply policies across an organization.

Cloud services and virtual desktops have also taken much of the effort out of provisioning the underlying environment. These are genuine advances, but they can create a false sense of completion. An application may open in the new environment and appear ready for production.

The problems tend to emerge later. An update arrives and the packaging process has to be recreated. An operating system change exposes a dependency that was never recorded. A certificate expires, or a new release behaves differently from the version originally tested.

None of these issues are solved by the fact that the application was delivered through a modern platform. Deployment gets an application to the user; modernization determines whether IT can continue to manage it once the project team has moved on.

## Old assumptions follow applications into new environments

Enterprise application estates tend to grow gradually. Software is added over many years, often under different teams and different versions of Windows. Some applications expect access to folders or registry locations that would not be considered appropriate today. Others rely on old runtimes, fixed paths or components installed so long ago that nobody is entirely sure why they are there. Accompanying IT documentation is rarely complete.

The original installer may have disappeared and the person who understood the application may no longer work for the organization, yet the software itself may remain essential to a finance team, production line or clinical process.

Moving to modern endpoint management such as Intune, a Cloud PC or a new virtual desktop environment does not remove those assumptions. In some cases, it exposes them because modern environments place tighter limits on what software is allowed to change. A launch test will reveal only part of the picture.

IT management also needs to know how the application installs, what it depends on, which parts of the system it expects to access and how it is updated and removed. Age alone is not a reason to replace an application. Many older line-of-business tools remain useful and business-critical. The aim should be to understand the software well enough to manage it properly, rather than carrying its old behavior into a new environment without examining it.

## Modernization does not have to mean rewriting software

Rewriting every legacy application would be impractical for most businesses and may deliver little value where the existing software still performs its function well. A better test is whether the application can be supported throughout the rest of its working life. That requires a clear view of its files, services, dependencies and interaction with Windows. Once those details are known, compatibility problems can be addressed deliberately rather than discovered by users after deployment.

Packaging is part of that work, although it is not the whole answer. On Windows, formats such as MSIX can give an application a clearer identity, require digital signing and separate more of its activity from the underlying operating system. They can also support cleaner removal and more controlled updates. MSIX can provide a more secure and manageable foundation, although applications with legacy middleware, undocumented dependencies or highly specialized configurations may still require additional work.

This is why organizations need to identify complex applications early. Testing must also reflect real use: opening the main window does not show whether employees can complete the tasks they rely on, whether the next update will install successfully or whether the application will continue working when another part of the environment changes.

The scope becomes clearer when organizations view the modern endpoint as a set of interconnected components. A desktop comprises three core elements: the operating system, the user profile, and applications. Hardware is the fourth component, but the same principles apply whether the machine is physical or virtual.

The applications work is therefore a project in its own right. Applications must be brought under control, secured, and kept up to date and delivered to the right users, with the control and compliance an organization requires.

## Bring applications into the project sooner

Applications are often treated as the last stage of an endpoint program. The platform is selected, the environment is built and only then does the organization begin working through the software estate. By that point, timelines have been agreed and assumptions about compatibility may already be built into the plan. Difficult applications emerge as late exceptions, when there is the least room to deal with them.

Bringing application assessment forward gives IT a clearer view of what it is migrating. Teams can establish which applications are in use, which are business-critical and which depend on technology that may not be available in the new environment. They can also separate routine applications from those requiring deeper technical or business knowledge.

I have worked in this industry since the late 1990s and have seen enterprise desktops move from early thin-client systems to virtual desktops and, more recently, cloud-hosted PCs. The infrastructure has improved enormously, but the questions around applications have barely changed.

A modern endpoint is an important step, but the real measure of modernization is whether the organization can understand, update and support the applications running on it.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
