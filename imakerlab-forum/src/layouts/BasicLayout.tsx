import React from 'react';
import type {BasicLayoutProps as ProLayoutProps, MenuDataItem} from '@ant-design/pro-layout';
import ProLayout from '@ant-design/pro-layout';
import SYSTEM_LOGO from '@/assets/logo.png';
import defaultSettings from '../../config/defaultSettings';
import menu from '../../config/headerMenu';
import type {AccessType} from '@/access';
import access from '@/access';
import {Link} from 'umi';
import RightContent from '@/components/RightContent';
import {DEFAULT_WEBSITE_NAME, DEFAULT_WEBSITE_URL} from "@/constant";

export interface BasicLayoutProps extends ProLayoutProps {
  route: ProLayoutProps['route'] & {
    authority: string[];
  };
}

/**
 * use Authorized check all menu item
 */
const menuDataRender = (menuList: MenuDataItem[], access: AccessType): MenuDataItem[] => {
  return menuList.filter((menuItem) => {
    return !menuItem.access || access[menuItem.access];
  });
};

const BasicLayout: React.FC<BasicLayoutProps> = (props) => {
  const {children} = props;

  return (
    <>
      <ProLayout
        logo={
          <>
            {/*<Popover*/}
            {/*  placement="topRight"*/}
            {/*  content={*/}
            {/*    <div>*/}
            {/*      <img width={200} src={save_site} alt="" />*/}
            {/*    </div>*/}
            {/*  }*/}
            {/*  title="拖拽Logo到收藏栏，刷题更方便！"*/}
            {/*>*/}
            <span>
                <a href={DEFAULT_WEBSITE_URL} title={DEFAULT_WEBSITE_NAME}>
                  <img
                    // style={{
                    //   width: '200px',
                    //   height : '200px'
                    // }}
                  src={SYSTEM_LOGO} alt={DEFAULT_WEBSITE_NAME} title={DEFAULT_WEBSITE_NAME} />
                </a>
              </span>
            {/*</Popover>*/}
          </>
        }
        {...props}
        {...defaultSettings}
        headerTheme="light"
        layout="mix"
        splitMenus
        menuItemRender={(menuItemProps, defaultDom) => {
          if (menuItemProps.isUrl || !menuItemProps.path) {
            return defaultDom;
          }
          return <Link to={menuItemProps.path}>{defaultDom}</Link>;
        }}
        menuDataRender={() => menuDataRender(menu, access)}
        rightContentRender={() => <RightContent/>}
      >
        {children}
      </ProLayout>
    </>
  );
};

export default BasicLayout;
