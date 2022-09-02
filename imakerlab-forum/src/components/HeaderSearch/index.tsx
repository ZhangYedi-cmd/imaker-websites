import { SearchOutlined } from '@ant-design/icons';
import type { InputRef } from 'antd';
import { AutoComplete, Col, Input } from 'antd';
import type { AutoCompleteProps } from 'antd/es/auto-complete';
import classNames from 'classnames';
import useMergedState from 'rc-util/es/hooks/useMergedState';
import React, { CSSProperties, useRef } from 'react';
import styles from './index.less';

export type HeaderSearchProps = {
  onSearch?: (value?: string) => void;
  onChange?: (value: string) => void;
  defaultValue?: string;
  value?: string;
  style?: CSSProperties;
  placeholder?: string;
};

const HeaderSearch: React.FC<HeaderSearchProps> = (props) => {
  const { style, placeholder, value, onChange } = props;

  const handleSearch = (): void => {
    console.log('search!');
  };

  return (
    <div style={{ display: 'flex' }}>
      <Input.Search
        style={{ height: '100%' }}
        placeholder={placeholder}
        size="large"
        maxLength={40}
        enterButton
        onSearch={handleSearch}
      />
    </div>
  );
};

export default HeaderSearch;
